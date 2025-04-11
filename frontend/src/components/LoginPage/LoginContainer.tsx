import React from 'react';

type Props = {
    children: React.ReactNode;
}

const LoginContainer = ({ children }: Props) => {
    return (
        <div className="login-container">
            {children}
        </div>
    )
}

export default LoginContainer;
export{};