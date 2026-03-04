import { useContext, createContext, useEffect, useState } from "react";
import { 
    GoogleAuthProvider,
    signOut,
    onAuthStateChanged,
    signInWithPopup, // CHANGED: Popup is much more stable than Redirect
} from "firebase/auth";

import {auth} from '../firebase';

const AuthContext = createContext();

export const AuthContextProvider = ({children}) => {
    const [user, setUser] = useState(null); // Start with null
    const [loading, setLoading] = useState(true); // 1. Added loading state

    const googleSignIn = async () => {
        const provider = new GoogleAuthProvider();
        // 2. Changed to signInWithPopup to prevent page reload bounce
        await signInWithPopup(auth, provider);
    } 

    const logOut = () => {
        signOut(auth).catch((error) => console.log(error));
    }

    useEffect(() => {
        const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
            setUser(currentUser);
            setLoading(false); // 3. Stop loading once Firebase answers
        });
        return () => unsubscribe();
    }, []);

    return (
        <AuthContext.Provider value={{ googleSignIn, logOut, user, loading }}>
            {!loading && children} {/* 4. ONLY show app after loading is done */}
        </AuthContext.Provider>
    )
}

export const UserAuth = () => {
    return useContext(AuthContext)
};