import React, { useState } from 'react';
import { Link, Navigate } from 'react-router-dom';
import { connect } from 'react-redux';
import { login } from '../../actions/auth';
import Alert from '@mui/material/Alert';
import axios from 'axios';

import "./Login.css"


const Login = ({ login, isAuthenticated }) => {
    const [error, setError] = useState('')

    const [formData, setFormData] = useState({
        email: '',
        password: ''
    });

    const { email, password } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });
   
    const onSubmit = async (e) => {
        e.preventDefault();

        try {
            
            await login(email, password);

        } catch (err) {
            const obj = JSON.parse(err.request.response)
            const message = obj[Object.keys(obj)[0]]
            setError(message)
        }
    };

    const continueWithGoogle = async () => {
        try {
            const res = await axios.get(`${process.env.REACT_APP_API_URL}/auth/o/google-oauth2/?redirect_uri=${process.env.REACT_APP_API_URL}/google`)

            window.location.replace(res.data.authorization_url);
        } catch (err) {

        }
    };

    const continueWithFacebook = async () => {
        try {
            const res = await axios.get(`${process.env.REACT_APP_API_URL}/auth/o/facebook/?redirect_uri=${process.env.REACT_APP_API_URL}/facebook`)

            window.location.replace(res.data.authorization_url);
        } catch (err) {

        }
    };

    if (isAuthenticated) {
        return <Navigate to='/' />
    }

    return (

        <div id='login-page'>
            <div className="container">
                <div className="d-flex justify-content-center h-100">
                    <div className="card">
                        <div className="card-header">
                            <h3>Sign In</h3>
                            <div className="d-flex justify-content-end social_icon">
                                <span onClick={continueWithFacebook}><i className="fab fa-facebook-square"></i></span>
                                <span onClick={continueWithGoogle}><i className="fab fa-google-plus-square"></i></span>
                            </div>
                        </div>
                        <div className="card-body">
                            <form onSubmit={e => onSubmit(e)}>
                                <div className="input-group form-group">
                                    <div className="input-group-prepend">
                                        <span className="input-group-text"><i className="fas fa-envelope"></i></span>
                                    </div>
                                    <input
                                        className='form-control'
                                        type='email'
                                        placeholder='Email'
                                        name='email'
                                        value={email}
                                        onChange={e => onChange(e)}
                                        required
                                    />
                                </div>
                                <div className="input-group form-group">
                                    <div className="input-group-prepend">
                                        <span className="input-group-text"><i className="fas fa-key"></i></span>
                                    </div>
                                    <input
                                        className="form-control"
                                        type='password'
                                        placeholder='Password'
                                        name='password'
                                        value={password}
                                        onChange={e => onChange(e)}
                                        minLength='6'
                                        required
                                    />
                                </div>
                                {/* <div className="row align-items-center remember">
                                    <input type="checkbox" />Remember Me
                                </div> */}
                                <div className="form-group">
                                    <input type="submit" value="Login" className="btn float-right login_btn" />
                                </div>
                            </form>
                        </div>
                        
                        <div>
                            {error && <Alert severity="error">{error}</Alert>}
                        </div>

                        <div className="card-footer">
                            <div className="d-flex justify-content-center links"> Don't have an account?
                                <Link to='/signup'>Sign Up</Link>
                            </div>
                            <div className="d-flex justify-content-center links">Forgot password?
                                <Link to='/reset-password'> Reset Password</Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { login })(Login);