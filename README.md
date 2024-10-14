README
Description:
The app is a basic school management system server that can be connected to by a client. The system can be used to create new class subjects, assign students and teachers to and delete them from class groups. The application has 3 roles these are admin, teacher and student each with different levels of security.
Usage requirements:
* IDE software (Visual Studio Etc.)
* All linked folders downloaded locally
* Python 
Libraries used (all python):
* Bcrypt
* Pytest 
* Socket.io
* Pydantic 

Installation and user guide: 
The application requires all the linked python files to be downloaded onto the local system. Below is a getting started guide.
1. Open the API.py file in an IDE make sure that the terminal is open. The API.py file can then be run which starts the server. When set up is complete the following messages shall appear in the terminal: 
Server listening on port 12345
SMS Created
SMS has been created

2. Next open the client Application.py file in an IDE making sure that the terminal is open. Run this file and the following message should appear in the terminal: 
Sending query:  sms.current_user    
Response recieved:  null
Please select one of the following: 
1-Log in 
2-Create new user
3. Next one of 2 options can be selected by typing in the corresponding number (‘1’ for log in and ‘2’ for create a new user). 
If ‘1 – log in’ is selected, then there are currently 3 different placeholder accounts that can be logged into for testing purposes. 
These are listed below with their username and password. 
Otherwise, if ‘2-create new user’ is selected a username and password will have to be created before the user will be sent back to the initial log on menu where they would then select ‘1-log in’ and enter the username and password they have just created. 
All new users are automatically assigned the role of a student this can be changed by an admin see point 6.
Preset usernames:defaultstudentdefaultteacherdefaultadmin
Preset password for all 3:password
4. Next once log in is complete the user will be presented with the main menu. Each option corresponds to a number and again the user should type the number for the option they wish to select. Below is a breakdown of the options and who can access which options. 
Menu OptionAccess1- View users and their rolesAll users2- Role editorOnly Admin users3- Manage subjectsAdmins and Teachers4- View your subjectsAll users5- Update security settingsOnly Admin users6- Log outAll users
5. It is recommended that the admin account is accessed first as this is used to assign the other accounts to subjects and without this the other accounts will not have proper access to the information they should have.
6. To complete set up as the admin the user will first need to select option ‘2’ from the main menu this will then display the following submenu seen below with a description of each potential action.
Menu OptionDescription1- Change a user’s roleThis will prompt allow the admin to change the role of a user. They can be changed to a ‘student’, ‘teacher’ or ‘admin’.2- Print all current users and their rolesThis will print all the current usernames registered on the system and their associated role.3- Delete a userThis will allow a user to be deleted from the system.4- Return to main menuThis will return the user to the main menu page this will be automatic if not an admin.It is recommended that the admin changes new users’ roles at this stage and checks that all users are assigned to the correct role before continuing.
7. Using the admin account the next option that should be accessed from the main menu is option 3 Manage subjects. 
There are currently 2 subjects preloaded into the system these are ‘French’ and ‘English’. When 3 is selected this will display a submenu detailed below:
Menu OptionDescription1- Add a subjectThis allows the admin to create a new subject that students and teachers can be assigned to.2- Print all subjectsThis prints a list of all the subjects currently on the system. This beings with just ‘French’ and ‘English.3- Print your subjectsThis prints the subjects assigned to the current user.4- Assign Teacher to subjectThis allows the admin to assign a teacher by their username to a subject.5- Assign Student to subjectThis allows the admin to assign a student by their username to a subject.6- Remove teacher or student from subjectThis will remove either a student or a teacher from a subject based on their username.7- Return to main menuThis will allow the user to return to the main menu. This will be automatic if you are not an Admin.
8. The final option that the user can select as the admin account is option 5 update security settings this will generate the question ‘Do you want to security settings to be <on> or <off>?’ this can be responded to with a ‘yes’ or a ‘no’. 
If yes is selected, then the security measures will be disabled and the system will be vulnerable to attack. 
9. The system can now be used with any account that has been created. Make sure that once the user is done they have selected option 6 to log out.

Additional Features: 
Hacking: A second client application can also be used to show different methods of hacking the server. This can be done through the running of the hacker_api.py file. This contains the software to perform a DDOS, Brute force and API injection attack on the system. 
CRUD: The program can perform CRUD functions for all the users created. Although the ability to perform the update and delete functions are only accessible to the admin to follow the GDPR guidelines of storing data securely.
Security: The program has been created with several security features in place such as password encryption and limiting access for certain accounts. This was done to protect the data stored within the system.
The system can be run with the security features switched on or off depending on what the system is to be used for. Only admin accounts have the ability to change the security settings, and they are set to on as the default. This can be changed by the admin by accessing ‘update security settings’ in the main menu.  
Other information:
This application has been created to adhere to GDPR guidelines (GDPR, 2016) and to follow the OWASP top 10 proactive controls for security (OWASP, 2024). See below for more details.

References: 
European Parliament and Council of the European Union. Regulation (EU) 2016/679 of the European Parliament and of the Council on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation). 
Available from: https://eur-lex.europa.eu/eli/reg/2016/679/oj [Accessed 11th October 2024].

OWASP (2024) OWASP Top 10 Proactive Controls. Available from: https://top10proactive.owasp.org/the-top-10/introduction/ [Accessed 11th October 2024].
2


