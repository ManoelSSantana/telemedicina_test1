import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';

export default function Login() {
    const [cpf, setCpf] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await api.post('/login', {
                username: cpf,
                password: password
            });
            
            localStorage.setItem('token', response.data.access_token);
            const role = JSON.parse(atob(response.data.access_token.split('.')[1])).role;
            
            switch(role) {
                case 'paciente':
                    navigate('/dashboard-paciente');
                    break;
                case 'medico':
                    navigate('/dashboard-medico');
                    break;
                case 'enfermeira':
                    navigate('/dashboard-enfermeira');
                    break;
            }
        } catch (error) {
            alert('Login failed');
        }
    };

    return (
        <div className="login-container">
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="CPF"
                    value={cpf}
                    onChange={(e) => setCpf(e.target.value)}
                />
                <input
                    type="password"
                    placeholder="Senha"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">Login</button>
            </form>
        </div>
    );
}
