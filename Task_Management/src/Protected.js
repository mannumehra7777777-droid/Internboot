import React from 'react';
import { Navigate } from 'react-router-dom';
import { UserAuth } from './context/AuthContext';

const Protected = ({ children }) => {
    const { user, loading } = UserAuth(); // You need 'loading' from your context

    // 1. If Firebase is still checking, show nothing or a spinner
    if (loading) {
        return <div>Loading...</div>; 
    }

    // 2. ONLY if loading is finished AND there is still no user, then redirect
    if (!user) {
        return <Navigate to='/' />;
    }

    return children;
};

export default Protected;