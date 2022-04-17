# AppleCart take home challenge

<h3> Background and Setup </h3>
This project was created in python3 so it is recommended it is installed along with the modules imported as shown in the questions.py file. I also created contacts.json and persons.json files using the examples from the question prompt. I created just enough entries in both files to ensure that my functions were working as inteded. Note: the solutions are not fully optimized and I present a possible solution in the Takeaway section at the bottom of the README. </br>
</br>

<h3> Running the program via command line </h3>
To run this program, the project folder must be in your current working directory once confirmed its in the correct directoy, you can now run the script through command line using the following: "python3 questions.py person_id" person_id being the id you want to find connections to. For example, running the command "python3 questions.py 5" will results in the following: </br> 
Jane Doe </br>
Tony Stark </br>
Bob Smith </br>
Isaac Newton </br>
</br>
Note: Tony Stark and Bob Smith are connected to the person_id ,5, through overlapping dates at a company of a minimum of 6 months. Jane Doe and Isaac Newton contain the phone number of person_id 5, so they are also connected. Not all id's will have connections, in which case nothing will print.</br>
</br>
<h3> Unit Testing </h3>
I unit tested the following functions:</br>
check_company_dates : this function checks if two experiences have overlapping dates of a minimum of 6 months.
</br>
normalize_phone : this function normalizes phone numbers to match the format of numbers in persons.json file. This function currently works in a narrow scope and doesn't currently handle all edge cases (eg. country codes that start with a number other than 1 and phone numbers starting with (XXX) format but not from the current country, etc.). Overall this function works for the numbers formatted in the contacts.json file. </br>
get_connected_people : this function was tested three different ways, once for getting connected people through company overlap only, once for getting connected people through contacts numbers only, and once for both. </br>
All tests are passing, see questions_test.py for test cases. I haven't refactored the test after implementing arg parser , so to run the unit tests you will need to comment out the lines mentioned in the questions.py file, on lines 7 & 89, save, the run the command "python3 -m unittest questions_test"

</br>
</br>
<h3>Take Aways </h3>
One thing I added to the prompt was including various experiences for a single person, the example shown in the prompt is shown as an array with a single object entry, but in reality there can be multiple experiences where a person can even leave a company and comeback a few years later. This added two nested for loops but breaks if an overlap is found because your just checking if the person has overlap with "other person" once an overlap is found that connection is there no matter what other experiences they both have. Because of the small files, the script runs in a resonable amount of time. However, for very large files, the run time will get exponentiolly long O(n^4). One of the longest operations is finding the correct id in the persons entry, this can be optimized by using a database and indexing the person_id column in a b-tree format. this makes the initial person_id search to be O(log n). checking every other entry for a connection is non negotiable so that has to be done O(n). in the original case where only one experience per person is listed, it wouldn't add any additional time complexity but I added lists of exps so O(n^2). with additional complexity total worst case run time is O(n^3 log n) without additional complexity (1 exp) it is O(n log n). This really gave me some insight into how Applecart works under the hood and the challenges of optimizing a lot of these types of prompts can have. Overall this was a very fun project!