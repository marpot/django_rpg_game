import React from 'react';
import LoginContainer from "./LoginContainer";
import LoginSection from "./LoginSection";
import { handleSubmit } from './SubmitHandler';

const LoginPageComponent = () => {
    return (
    <LoginContainer>
        <LoginSection errorMessage='' onSubmit={handleSubmit} />
    </LoginContainer>
  );
};
export default LoginPageComponent;
export{};
