import { useState } from 'react'
import SelectButton from './components/find/find'
import Navbar from './components/navbar/navbar'
import Title from './components/title/title'
import Footer from './components/footer/footer'
import './App.css'

function App() {
  //  const [count, setCount] = useState(0)

  return (
    <>
        <div className='bg'>
      <Title />
      <br></br><br></br>
      <Navbar />
      <br></br>
      <SelectButton />
      <Footer/>
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
    </>
  )
}

export default App
