import { useEffect, useState } from 'react'
import Navbar from './components/navbar/navbar'
import Title from './components/title/title'
import Para from './components/para/para'
import DropDown from './components/find/find'
import Table from './components/table/Table'
import Footer from './components/footer/footer'
import './App.css'

function App() {


  const [farmer, setCount] = useState(0)
const [data, setData] = useState([])
const [id, setId]=useState(null)


  async function getfarmercompanies() {
    const fetched = await fetch("http://127.0.0.1:8000/farmercompany/")
    const farmercompanies = await fetched.json()
    console.log(farmercompanies.data[0])
    const datafetched =farmercompanies.data[0]
    setData(datafetched)
  }

  useEffect(() => {
    getfarmercompanies()
  },
    []
  )

console.log(data)
console.log(id)
  return (
    <>
      <div className='bg'>
        <br></br>
        <Title />
        <br></br><br></br>
        <Navbar />
        <br></br>
        <Para />
        <br></br>
        <div className='button'>
          <DropDown data={data} findid={setId} companyid={id}/>
        </div>
        <Table foundid={id} />
      </div>
      <Footer />
    </>
  )
}

export default App
