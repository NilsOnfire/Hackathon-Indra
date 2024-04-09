import React from 'react';
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import FormPage from './pages/FormPage'
import HomePage from './pages/HomePage'
function App(){
  return(
   <BrowserRouter>
   <Routes>
     <Route path="/" element={<HomePage />} />
     <Route path="/user/new" element={<FormPage />} />
   </Routes>
   </BrowserRouter>
  )
}
export default App;