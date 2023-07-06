import React, { useEffect } from 'react';
import Navbar from '../components/Navbar';
import { connect } from 'react-redux';
import { checkAuthenticated, load_user, user_preference_retrieve } from '../actions/auth';
import { useLocation } from 'react-router-dom';

const Layout = ({ checkAuthenticated, load_user, user_preference_retrieve, children, isAuthenticated }) => {

    const location = useLocation();
    const isLoginOrSignup = location.pathname === '/login' ||
        location.pathname === '/signup' || 
        location.pathname === '/reset-password' ||
        location.pathname === '/password/reset/confirm/:uid/:token' ||
        location.pathname === '/activate/:uid/:token' || 
        location.pathname === '/email/info';

    useEffect(() => {
        checkAuthenticated();
        load_user();
        user_preference_retrieve();
    }, []);

    return (
        <div>
            {!isLoginOrSignup && <Navbar />}
            {children}
        </div>
    );
};

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});


export default connect(mapStateToProps, { checkAuthenticated, load_user, user_preference_retrieve })(Layout);