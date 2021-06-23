# Command_line_book_search
Repository for a command line based search tool that utilizes the Google Books Api and a command line interface with Python.

# Welcome to the Google Books Search Tool!

### This repository is for a command line based search tool that utilizes the Google Books Api and a command line interface with Python.
#### For best results, have your terminal opened in a large viewing window.
#### Install dependencies:
```console
pip install -r requirements.txt
```
#### How to use:
##### - To use this search tool, simply clone, download, or copy the repository onto your local machine.
##### - Run the file requests.py and follow the prompts 
```console
$ python3 book_search.py 
```
##### - You will see the prompts begin immediately
```console
 
░█▀▄░█▀█░█▀█░█░█        
░█▀▄░█░█░█░█░█▀▄        
░▀▀░░▀▀▀░▀▀▀░▀░▀        
░█▀▀░█▀▀░█▀█░█▀▄░█▀▀░█░█
░▀▀█░█▀▀░█▀█░█▀▄░█░░░█▀█
░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀                                                                        
    
Hello! Welcome to the Google Books Command Line Search Tool! 

I look forward to helping you create a list of your next great reads! 
 
Please enter your search, without spaces. 
 

```
##### - Continue to follow the prompts to search and add books to your list!
```console
cats
SEARCH RESULTS 


+----+------------------------+------------------------+-----------------------+
| Id |         Title          |       Author(s)        |       Publisher       |
+====+========================+========================+=======================+
| 1  | Oi Frog!               | ['Kes Gray']           | Hodder Children's     |
|    |                        |                        | Books                 |
+----+------------------------+------------------------+-----------------------+
| 2  | 12 Rules for Life      | ['Jordan B. Peterson'] | Ballantine Books      |
+----+------------------------+------------------------+-----------------------+
| 3  | Happy Birthday, Bad    | ['Nick Bruel']         | Roaring Brook Press   |
|    | Kitty                  |                        |                       |
+----+------------------------+------------------------+-----------------------+
| 4  | Nala's World           | ['Dean Nicholson']     | Grand Central         |
|    |                        |                        | Publishing            |
+----+------------------------+------------------------+-----------------------+
| 5  | Some Pets              | ['Angela DiTerlizzi']  | Simon and Schuster    |
+----+------------------------+------------------------+-----------------------+


READING LIST 

```
### Testing
- In order to ensure that further changes and improvements can be made, there are test files that can be run.
- To run a test file, just run the test file name:
```console
$ python3 test_clean_search_methods.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.052s

OK
```
- If you would like more verbose results, append -v to the end of the command:
```console
$ python3 test_clean_search_methods.py -v 
test_clean_search (__main__.TestCleanSearchMethods) ... ok
test_remove_emoji (__main__.TestCleanSearchMethods) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.050s

OK
```

Tests that pass will give an okay, and ones that fail will follow suit.
```console
$ python3 test_clean_search_methods.py -v 
test_clean_search (__main__.TestCleanSearchMethods) ... FAIL
test_remove_emoji (__main__.TestCleanSearchMethods) ... ok

======================================================================
FAIL: test_clean_search (__main__.TestCleanSearchMethods)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/user/8th_light/books_8th_light/test_clean_search_methods.py", line 22, in test_clean_search
    self.assertEqual(clean_search("Dance  ""   !"), "Da nce!")
AssertionError: 'Dance!' != 'Da nce!'
- Dance!
+ Da nce!
?   +


----------------------------------------------------------------------
Ran 2 tests in 0.063s

```

Thanks for using my command line search tool!
