// Design a generic system which can handle addition of new attributes

----- 
	SAAS 
  managing vehicle data
  	- different attributes
    - 

    
GenericVehicle
	- id 
  - client_id



VehicleCustomAttribute
	- id
	- generic_id
  - name varchar  
	- value varchar
  - created_at
  - last_updation_date

(12, 112121, "color", "red", "10DEC", "5DEC")
(12, 112121, "color", "black", "5DEC", "1DEC")
(12, 112121, "color", "green", "1DEC", "1DEC")


Version
	- id
  -
  - diff - "{}"
  - created_at index
  

(11, 12, "{"color": ["red", "black"]}", 10DEC)
(10, 12, "{"color": ["black", "green"]}", 5DEC)
(10, 12, "{"color": ["black", "green"]}", 1DEC)

(9, 12, "{"color": ["green", null]}", 1DEC)

int, string, boolean, double, float

array, 
attr1 => []

# find attrrs value on a given particular date for a vehicle id

row = select * from attribute_versions where vehicle_id = 12121 and created_at <= datetime order by created_at DESC limit 1;
row.diff.color

Color attr 
1 Dec - green
5 dec - black
10 dec - red

1  color green 1-dec
1  color green 5-dec
1  color green 10-dec

select * from VehicleCustomAttribute where attr_name = 'attr' and vehicle_id = 12121 and last_updation_date =< date <= created_at;


