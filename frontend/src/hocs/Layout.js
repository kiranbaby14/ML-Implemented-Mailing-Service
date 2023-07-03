import React, { useEffect } from 'react';
import Navbar from '../components/Navbar';
import { connect } from 'react-redux';
import { checkAuthenticated, load_user } from '../actions/auth';
import { useLocation } from 'react-router-dom';

const Layout = ({ checkAuthenticated, load_user, children, isAuthenticated }) => {

    const location = useLocation();
    const isLoginOrSignup = location.pathname === '/login' || location.pathname === '/signup';

    useEffect(() => {
        checkAuthenticated();
        load_user();
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


export default connect(mapStateToProps, { checkAuthenticated, load_user })(Layout);