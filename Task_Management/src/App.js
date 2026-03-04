import React from "react";
import { Routes, Route, useLocation } from "react-router-dom"
import Login from "./Login";
import TodoPage from "./TodoPage";
import { AuthContextProvider } from './context/AuthContext'
import Protected from "./Protected";




function App() {
  return (
    <div>
      <AuthContextProvider>
        <Routes>
          {/* Main Login Route */}
          <Route path='/' element={<Login />} />
          
          {/* Protected Todo Route */}
          <Route 
            path='/todos' 
            element={
              <Protected>
                <TodoPage />
              </Protected>
            } 
          />
        </Routes>
      </AuthContextProvider>
    </div>
  );
}

export default App;
