// Import the functions you need from the SDKs you need

import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

import { getFirestore } from "firebase/firestore";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAq629bVXfS_FF7x-DVXDcCE9zA_W33n5U",
  authDomain: "task-management-1f349.firebaseapp.com",
  projectId: "task-management-1f349",
  storageBucket: "task-management-1f349.firebasestorage.app",
  messagingSenderId: "898505840438",
  appId: "1:898505840438:web:c3206cf9613b43d6770597",
  measurementId: "G-9KC4SNEPQZ"
};
// Initialize Firebase
const app = initializeApp(firebaseConfig)
//initialize authentication to get reference to service
export const auth = getAuth(app);

// export database firestore 
export const db = getFirestore(app);