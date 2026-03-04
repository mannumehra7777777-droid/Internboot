import {React, useEffect } from "react";
import { UserAuth} from "./context/AuthContext";
import {useNavigate} from 'react-router-dom';
import todopic from './images/todopic.jpeg';



const Login = () => {
    const { googleSignIn, user } = UserAuth();
    const navigate = useNavigate();

    const handleGoogleSignIn = async () => {
        try {
            await googleSignIn()
        } catch(err) {
            console.log(err);
        }
    }
    useEffect(() => {
        if (user) {
            navigate('/todos');
        } 
    },[navigate, user])

    return (
    <section className="bg-gray-50 min-h-screen flex items-center justify-center
        ">
        {/* login container */}
        <div  className="bg-gray-100 flex rounded-2xl shadow-lg p-5 max-w-3xl items-center">
                {/* welcome title */}

    
    
          <div className="md:w-1/2 px-16">
          <h2 className="font-bold text-3xl mb-10">Welcome to  
          <br/>
          To Do Pro</h2> 

           {/*  */}
         <button className="bg-white border py-2 px-3 w-full rounded-xl mt-7 flex justify-center items-center text-m"  onClick={handleGoogleSignIn}>
            {/* google svg */}
         <svg className="mr-3" viewBox="0 0 48 48" width="50px" height="50px">
  <title>Google Logo</title>
  <clipPath id="g">
    <path d="M44.5 20H24v8.5h11.8C34.7 33.9 30.1 37 24 37c-7.2 0-13-5.8-13-13s5.8-13 13-13c3.1 0 5.9 1.1 8.1 2.9l6.4-6.4C34.6 4.1 29.6 2 24 2 11.8 2 2 11.8 2 24s9.8 22 22 22c11 0 21-8 21-22 0-1.3-.2-2.7-.5-4z"/>
  </clipPath>
  <g className="colors" clipPath="url(#g)">
    <path fill="#FBBC05" d="M0 37V11l17 13z"/>
    <path fill="#EA4335" d="M0 11l17 13 7-6.1L48 14V0H0z"/>
    <path fill="#34A853" d="M0 37l30-23 7.9 1L48 0v48H0z"/>
    <path fill="#4285F4" d="M48 48L17 24l-4-3 35-10z"/>
  </g>
</svg>
        Sign in with Google 
        </button>  
            </div>
    {/* image */}
        <div className="w-1/2 ">
            <img className="rounded-2xl" src={todopic} alt="todolist" />
        </div>
    </div>
    </section>
    );
}

export default Login;