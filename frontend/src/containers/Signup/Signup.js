import React, { useState } from 'react';
import { Link, Navigate } from 'react-router-dom';
import { connect } from 'react-redux';
import { signup } from '../../actions/auth';
import Alert from '@mui/material/Alert';
import axios from 'axios';

import './Signup.css'


const Signup = ({ signup, isAuthenticated }) => {

    const [error, setError] = useState('')

    const [accountCreated, setAccountCreated] = useState(false);
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
        re_password: ''
    });

    const { name, email, password, re_password } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = async (e) => {
        e.preventDefault();

        if (password === re_password) {
            try {
                await signup(name, email, password, re_password);
                setAccountCreated(true);
            } catch (err) {
                const obj = JSON.parse(err.request.response)
                const message = obj[Object.keys(obj)[0]]
                setError(message)
            }

        } else {
            setError("Password does not match")
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
    if (accountCreated) {
        return <Navigate to='/email/info' />
    }

    return (
        <div id='signup-page'>
            <div className="container">
                <div className="d-flex justify-content-center h-100">
                    <div className="card">
                        <div className="card-header">
                            <h3>SIgnUp</h3>
                            {/* <h3>Create your Account</h3> */}
                        </div>
                        <div className="card-body">
                            <form onSubmit={e => onSubmit(e)}>
                                <div className="input-group form-group">
                                    <div className="input-group-prepend">
                                        <span className="input-group-text"><i className="fas fa-user"></i></span>
                                    </div>
                                    <input
                                        className='form-control'
                                        type='text'
                                        placeholder='Name'
                                        name='name'
                                        value={name}
                                        onChange={e => onChange(e)}
                                        required
                                    />
                                </div>
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
                                        className='form-control'
                                        type='password'
                                        placeholder='Password'
                                        name='password'
                                        value={password}
                                        onChange={e => onChange(e)}
                                        minLength='6'
                                        required
                                    />
                                </div>
                                <div className="input-group form-group">
                                    <div className="input-group-prepend">
                                        <span className="input-group-text"><i className="fas fa-key"></i></span>
                                    </div>
                                    <input
                                        className='form-control'
                                        type='password'
                                        placeholder='Confirm Password'
                                        name='re_password'
                                        value={re_password}
                                        onChange={e => onChange(e)}
                                        minLength='6'
                                        required
                                    />
                                </div>

                                <div className="form-group">
                                    <input type="submit" value="Register" className="btn float-right login_btn" />
                                </div>
                            </form>
                        </div>

                        <div>
                            {error && <Alert severity="error">{error}</Alert>}
                        </div>

                        <div className="horizontal-line-container">
                            <div className="horizontal-line"></div>
                            <div className="or-text">Or</div>
                        </div>
                        <button className='btn btn-danger mt-4' onClick={continueWithGoogle}>
                            Continue With Google
                        </button>
                        <br />
                        <button className='btn btn-primary ' onClick={continueWithFacebook}>
                            Continue With Facebook
                        </button>
                        <div className="card-footer">
                            <div className="d-flex justify-content-center links"> Already have an account?
                                <Link to='/login'>Sign In</Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { signup })(Signup);