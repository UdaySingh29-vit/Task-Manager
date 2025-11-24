# |Problem Statement|
In a fast-paced digital environment, users often get overwhelmed by complex productivity apps with too many features. <br>
There is a need for a minimalist, distraction-free tool that allows users to quickly jot down and manage tasks directly from their developer environment (the terminal) without needing to open a web browser or heavy GUI application.

# |Scope of the Project|
The project is limited to a Command Line Interface (CLI). It focuses on the core "CRUD" (Create, Read, Delete) functionalities.<br>
---In Scope: Adding tasks, listing tasks, deleting tasks by index. <br>
---Out of Scope: Graphical User Interface (GUI), deadlines/reminders, user authentication, saving data to a local text file, or cloud synchronization.

# |Target Users|
---Developers & Sysadmins: Users who prefer staying in the terminal environment.<br>
---Students: Those learning Python.<br>
---Minimalists: Users seeking a lightweight alternative to complex project management software.

# High level Features
* **Task Creation (Input):** Allows the user to quickly add one or more new tasks to the active To-Do list using the add_task() function (Menu Option 1).
* **Task Completion (Status Change):** Enables the user to mark a specific task as done, which automatically removes it from the To-Do list and archives it in the Done list using the done_task() function (Menu Option 2).
* **Task Reporting/Viewing:** Provides a snapshot display of both the pending To-Do list and the completed Done list using the show() function (Menu Option 3).
* **Application Exit:** Safely terminates the program, offering a final summary of remaining tasks before closing via the exits() function (Menu Option 4).
