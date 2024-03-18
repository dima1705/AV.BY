import './App.css'

import { Navbar } from "./components/Navbar/Navbar";
import { Routes, Route } from "react-router-dom";
import { Transport,
  Examples,
  Parts_and_tyres,
  Journal, 
  Finance, 
  Knowledge, 
  AdvertPage,
  VIN,
  SinglePage,
  LoginPage,
  RegistrationPage} from "./pages";



function App() {

  return (
    <div className="App">
      <Navbar/>
      <Routes>
        {/* <Route path="/" element={<Examples/>}/> */}
        <Route path="/:brand/:model/:id" element={<SinglePage/>}/>
        <Route path="/" element={<Transport/>}/>
        <Route path="/parts_and_tyres" element={<Parts_and_tyres/>}/>
        <Route path="/journal" element={<Journal/>}/>
        <Route path="/finance" element={<Finance/>}/>
        <Route path="/knowledge" element={<Knowledge/>}/>
        <Route path="/advertPage" element={<AdvertPage/>}/>
        <Route path="/loginPage" element={<LoginPage/>}/>
        <Route path="/registrationPage" element={<RegistrationPage/>}/>
        <Route path="/VIN" element={<VIN/>}/>

      </Routes>
    </div>
  );
}

export default App;
