import React from 'react';

interface LoginErrorProps {
  errorMessage?: string;
}

const LoginError: React.FC<LoginErrorProps> = ({ errorMessage }) => {
  return (
    <p style={{ color: 'red' }}>{errorMessage}</p>
  );
};

export default LoginError;
export{};