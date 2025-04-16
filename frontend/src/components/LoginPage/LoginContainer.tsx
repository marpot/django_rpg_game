import React from 'react';
import styles from '../css/login-dark.scss';

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