import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Layout from './hocs/Layout';
import Home from './containers/Home/Home'
import Login from './containers/Login/Login'
import Signup from './containers/Signup/Signup'
import ResetPassword from './containers/ResetPassword'
import ResetPasswordConfirm from './containers/ResetPasswordConfirm'
import Activate from './containers/Activate'

import { Provider } from 'react-redux';
import store from './store';
import EmailInfo from './containers/EmailInfo';

function App() {

  return (
    <Provider store={store}>
      <BrowserRouter>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path='/login' element={<Login />} />
            <Route path='/signup' element={<Signup />} />
            {/* <Route path='/facebook' element={Facebook} />
          <Route path='/google' element={Google} /> */}
            <Route path='/reset-password' element={<ResetPassword />} />
            <Route path='/password/reset/confirm/:uid/:token' element={<ResetPasswordConfirm />} />
            <Route path='/activate/:uid/:token' element={<Activate />} />
            <Route path='/email/info' element={<EmailInfo />} />
          </Routes>
        </Layout>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
