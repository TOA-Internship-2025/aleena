import { useState } from 'react'
import Navbar from './components/navbar/navbar'
import Title from './components/title/title'
import Para from './components/para/para'
import DropDown from './components/find/find'
import Table from './components/table/Table'
import Footer from './components/footer/footer'
import './App.css'

function App() {
  //  const [count, setCount] = useState(0)

  return (
    <>
        <div className='bg'>
          <br></br>
      <Title />
      <br></br><br></br>
      <Navbar />
      <br></br>
      <Para/>
      <br></br>
      <div className='button'>  <DropDown/></div>
      <Table/>
    
    
      {/* <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div> */}
    </div>
    <Footer/>
    </>
  )
}

export default App
