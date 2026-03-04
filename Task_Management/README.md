# React.js To-Do App with Firebase Authentication and Cloud Storage

Welcome to my React.js To-Do App, a dynamic and secure task manager powered by Firebase Google Authentication and real-time Firestore cloud storage. This project demonstrates my proficiency as a junior developer in building modern, secure and responsive web applications.

<img width="1017" alt="todologinpic" src="https://github.com/tylercodes-11/react-firebase-todoapp/assets/96836274/04dc9029-fe32-4d3c-b2de-6bc8249f2247">


## Features

- **User Authentication:** Utilizes Firebase Google Authentication for secure user login and registration.

- **Real-time Data Sync:** Utilizes Firestore Cloud Storage to ensure real-time synchronization of tasks for each user.

- **Responsive Design:** Designed with a clean and intuitive user interface using Tailwind CSS for a seamless user experience on various devices.

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/tyler-codes11/react-firebase-todoapp.git
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Configure Firebase:
   - Create a Firebase project.
   - Add your Firebase configuration details in `src/firebase.js`.

4. Start the application:
   ```
   npm start
  
   ```
5. Start Server:
   ```
   node server.js

   ```
##
   <img width="967" alt="Screenshot 2023-09-12 at 3 15 43 PM" src="https://github.com/tylercodes-11/react-firebase-todoapp/assets/96836274/edb30aa0-fc36-41b5-bac7-89bc40291d33">


## Problems Encountered and Resolution

During the development of this CRUD app, I encountered a challenge when adding an asynchronous function to the `useEffect` within the Read component. To ensure a smooth user experience and prevent errors, I resolved this issue by placing the async function within the `useEffect` and including necessary conditional checks to ensure the user object is defined before proceeding with data retrieval.

This experience demonstrates my problem-solving abilities and determination to deliver a polished, error-free application.

Thank you for considering my project as a testament to my skills as a junior developer. Feel free to reach out if you have any questions or require further information.
