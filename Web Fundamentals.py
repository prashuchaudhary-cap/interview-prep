------------------------------------------------------------------------
        What happens when you type google.com
------------------------------------------------------------------------
https://github.com/alex/what-happens-when


What Is The OSI Model?
------------------------------------------------------------------------
https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/


Why is HTTP not secure? | HTTP vs. HTTPS
------------------------------------------------------------------------
https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/
https://www.keycdn.com/blog/difference-between-http-and-https

--
    HTTP operates at application layer, while HTTPS operates at transport layer.

--
    HTTPS transmits its data security using an encrypted connection. Basically it uses a public key which is then decrypted on the recipient side. The public key is deployed on the server, and included in what you know as an SSL certificate.

--
    The certificates are cryptographically signed by a Certificate Authority (CA), and each browser has a list of CAs it implicitly trusts. Any certificate signed by a CA in the trusted list is given a green padlock lock in the browser's address bar, because it's proven to be "trusted" and belongs to that domain.



SSL certificates include:
------------------------------------------------------------------------
The domain name that the certificate was issued for
Which person, organization, or device it was issued to
Which certificate authority issued it
The certificate authority`s digital signature
Associated subdomains
Issue date of the certificate
Expiration date of the certificate
The public key (the private key is kept secret)


Browsers and Certificate Validation
------------------------------------------------------------------------
https://www.ssl.com/article/browsers-and-certificate-validation/


What are the different types of encryption?
------------------------------------------------------------------------
The two main kinds of encryption are symmetric encryption and asymmetric encryption.
Asymmetric encryption is also known as public key encryption.

In symmetric encryption, there is only one key, and all communicating parties use the same key for encryption and decryption.

In asymmetric, or public key, encryption, there are two keys: one key is used for encryption, and a different key is used for decryption.
Either key can be used for either action, but data encrypted with the first key can only be decrypted
with the second key, and vice versa. One key is kept private, while one key is shared publicly, for anyone to use
– hence the "public key" name. Asymmetric encryption is a foundational technology for SSL (TLS).



How does SSL/TLS work?
------------------------------------------------------------------------
--
    Privacy -- SSL encrypts data that is transmitted across the web. This means that anyone who tries to intercept this data will only see a garbled mix of characters that’s nearly impossible to decrypt.
--
    authentication -- SSL initiates an authentication process called a handshake between two communicating devices to ensure that both devices are really who they claim to be.
--
    data integrity -- SSL also digitally signs data in order to provide data integrity, verifying that the data is not tampered with before reaching its intended recipient.



How does TLS work?
------------------------------------------------------------------------

TLS can be used on top of a transport-layer security protocol like TCP. There are three main components to TLS: Encryption, Authentication, and Integrity.

Encryption: hides the data being transferred from third parties.
Authentication: ensures that the parties exchanging information are who they claim to be.
Integrity: verifies that the data has not been forged or tampered with.
A TLS connection is initiated using a sequence known as the TLS handshake. The TLS handshake establishes a cypher suite for each communication session. The cypher suite is a set of algorithms that specifies details such as which shared encryption keys, or session keys, will be used for that particular session. TLS is able to set the matching session keys over an unencrypted channel thanks to a technology known as public key cryptography.

The handshake also handles authentication, which usually consists of the server proving its identity to the client. This is done using public keys. Public keys are encryption keys that use one-way encryption, meaning that anyone can unscramble data encrypted with the private key to ensure its authenticity, but only the original sender can encrypt data with the private key.

Once data is encrypted and authenticated, it is then signed with a message authentication code (MAC). The recipient can then verify the MAC to ensure the integrity of the data. This is kind of like the tamper-proof foil found on a bottle of aspirin; the consumer knows no one has tampered with their medicine because the foil is intact when they purchase it.




SSL Handshake
------------------------------------------------------------------------
https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/
https://www.thesslstore.com/blog/explaining-ssl-handshake/


