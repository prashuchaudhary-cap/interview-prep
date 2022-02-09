from enum import Enum, unique

@unique
class CampaignType(Enum):
    CALL = "CALL"
    TEXT = "TEXT"
    EMAIL = "EMAIL"
    LEAD_UPDATE = "LEAD_UPDATE"
    IVR = "IVR"


@unique
class GenderType(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


@unique
class StateType(Enum):
    S1 = "S1"
    S2 = "S2"
    S3 = "S3"


@unique
class ExecutionState(Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class BaseCampaign(object):
    def __init__(self, name, script, ctype=None):
        self.name = name
        self.script = script
        self.type = ctype

    def format_script(self, lead):
        return self.script.format(lead.name)

    def execute(self, lead):
        pass


class CallingCampaign(BaseCampaign):
    def __init__(self, name, script):
        super().__init__(name, script, CampaignType.CALL)

    def execute(self, lead):
        return f"Calling lead with phone number in Call Campaign {self.name} {lead.phone_number}"


class TextingCampaign(BaseCampaign):
    def __init__(self, name, script):
        super().__init__(name, script, CampaignType.TEXT)

    def execute(self, lead):
        return f"Texting lead with phone number in Text Campaign {self.name} {lead.phone_number}"


class EmailCampaign(BaseCampaign):
    def __init__(self, name, script):
        super().__init__(name, script, CampaignType.EMAIL)

    def execute(self, lead):
        return f"Emailing lead with Email in Email Campaign {self.name} {lead.phone_number}"


class LeadUpdateCampaign(BaseCampaign):
    def __init__(self, name, script):
        super().__init__(name, script, CampaignType.LEAD_UPDATE)

    def execute(self, lead):
        return f"Lead Update with phone number in LeadUpdate Campaign {self.name} {lead.phone_number}"


class IVRCampaign(BaseCampaign):
    def __init__(self, name, script):
        super().__init__(name, script, CampaignType.IVR)

    def execute(self, lead):
        return f"IVR lead with phone number in IVR Campaign {self.name} {lead.phone_number}"


class Lead(object):
    def __init__(self, name, phone_number, **kwargs):
        self.name = name
        self.phone_number = phone_number
        self.meta = kwargs

    def metadata(self):
        return {
            'age': self.meta.get('age'),
            'gender': self.meta.get('gender'),
            'state': self.meta.get('state')
        }


class WorkflowNode(object):
    def __init__(self, level, campaign):
        self.next = None
        self.level = level
        self.next_nodes = []
        self.condition = None
        self.campaign = campaign

    def run(self, lead):
        message = self.campaign.execute(lead=lead)
        print(message)
        self.__compute_next(lead=lead)

    def __has_branch(self):
        return len(self.next_nodes) == 2

    def __compute_next(self, lead):
        if not self.next_nodes:
            return

        if not self.__has_branch() or not self.condition:
            self.next = self.next_nodes[0]
            return

        meta = lead.metadata()
        if eval(self.condition, meta):
            self.next = self.next_nodes[0]
        else:
            self.next = self.next_nodes[1]

    def add_children(self, node):
        self.next_nodes.append(node)

    def set_condition(self, condition):
        self.condition = condition


class Workflow(object):
    def __init__(self):
        self.root = None
        self.nodes = []

    def process(self, lead):
        max_cycles_per_lead = 3
        current = self.root
        current.run(lead=lead)

        while current.next:
            previous_node_level = current.level
            current = current.next

            if current.level < previous_node_level:
                max_cycles_per_lead -= 1

            if max_cycles_per_lead == 0:
                print("Max Cycles Limit reached")
                break

            current.run(lead=lead)

    def add_node(self, campaign, level):
        node = WorkflowNode(campaign=campaign, level=level)
        if not self.root:
            self.root = node

        self.nodes.append(node)
        return node

    def max_level(self):
        return max(map(lambda n: n.level, self.nodes))

    def leaf_nodes(self):
        return list(filter(lambda n: n.level == self.max_level(), self.nodes))


class WorkflowRunner(object):
    def __init__(self, workflow, leads):
        self.leads = leads
        self.workflow = workflow

    def run(self):
        for lead in self.leads:
            self.workflow.process(lead=lead)


c1 = CallingCampaign("c1", "Hello sir/madam, how are you doing today? I'm calling from blah blah blah....")
c2 = CallingCampaign("c2", "Hello sir/madam, csd fd mdf df sdfd xcs sxs asaa sas as ax scs....")

t1 = TextingCampaign("t1", "Hey {name}, we have an offer for you blah blah blah..")
t2 = TextingCampaign("t2", "Hey {name}, trrt rt rtr fdfd bmf mfm m mmds mdsw..")

e1 = EmailCampaign("e1", "Hey {name}, we have an offer for you blah blah blah..")
e2 = EmailCampaign("e2", "Hey {name}, ewee weee wrw r rewr ewr r ewr we rwe rer  we rr erw.")

i1 = IVRCampaign("i1", "Hey {name}, IVR we have an offer for you blah blah blah..")
i2 = IVRCampaign("i2", "Hey {name}, IVR ewee weee wrw r rewr ewr r ewr we rwe rer  we rr erw.")

lead1 = Lead(phone_number=9980890006, name="Ramesh", email="ramesh@suresh.com", age=20, gender=GenderType.MALE.value, state=StateType.S1.value)
lead2 = Lead(phone_number=9880891008, name="Suresh", email="suresh@ramesh.com", age=55, gender=GenderType.MALE.value, state=StateType.S2.value)
lead3 = Lead(phone_number=9880891010, name="Mahima", email="mahima@gmail.com", age=26, gender=GenderType.FEMALE.value, state=StateType.S3.value)


# Basic Linear Workflow
workflow = Workflow()
node = workflow.add_node(campaign=c1, level=0)
node1 = workflow.add_node(campaign=t1, level=1)
node2 = workflow.add_node(campaign=e1, level=2)
node.add_children(node1)
node1.add_children(node2)
workflow.process(lead=lead1)


workflow.max_level()
workflow.leaf_nodes()


# Branch Workflow
workflow1 = Workflow(campaign=c1)
node = workflow1.root
node.set_condition(condition="age > 50")
node1 = workflow1.add_node(campaign=t1, level=1)
node2 = workflow1.add_node(campaign=t2, level=1)
node.add_children(node1)
node.add_children(node2)
workflow1.process(lead=lead1)
workflow1.process(lead=lead2)

# Branch Workflow with Converge
workflow2 = Workflow(campaign=c2)
node = workflow2.root
node.set_condition(condition="gender == 'MALE'")
node1 = workflow2.add_node(campaign=t1, level=1)
node2 = workflow2.add_node(campaign=t2, level=1)
node3 = workflow2.add_node(campaign=e2, level=2)
node.add_children(node1)
node.add_children(node2)
node1.add_children(node3)
node2.add_children(node3)
workflow2.process(lead=lead2)
workflow2.process(lead=lead3)


# Branch Workflow with Cycle
workflow3 = Workflow(campaign=c1)
node = workflow3.root
node1 = workflow3.add_node(campaign=t1, level=1)
node2 = workflow3.add_node(campaign=e2, level=2)
node3 = workflow3.add_node(campaign=i2, level=3)
node.add_children(node1)
node1.add_children(node2)
node2.add_children(node3)
node2.add_children(node)
node2.set_condition(condition="state == 'S1'")

workflow3.process(lead=lead1)
workflow3.process(lead=lead2)

