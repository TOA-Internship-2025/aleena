import { useEffect, useState } from 'react'
import Navbar from './components/navbar/navbar'
import Title from './components/title/title'
import Para from './components/para/para'
import DropDown from './components/find/find'
import Table from './components/table/table'
import Footer from './components/footer/footer'
import './App.css'

function App() {


  const [farmer, setCount] = useState(0)
const [data, setData] = useState([])
const [id, setId]=useState(null)
const [tabledata, setTableData]=useState([])

  async function getfarmercompanies() {
    const fetched = await fetch("http://127.0.0.1:8000/farmercompany/")
    const farmercompanies = await fetched.json()
    const datafetched =farmercompanies.data[0]
    setData(datafetched)
  }
  async function getcultivators() {
    const fetched = await fetch(`http://127.0.0.1:8000/cultivators/farmer/${id}`)
    const cultivators = await fetched.json()
    console.log("cultivatorsss",cultivators)
    try{
      const datafetched =cultivators.data[0]
      setTableData(datafetched)
    }
    catch{
      setTableData([])
    } 
  }

  useEffect(() => {
    getfarmercompanies()
  },
    []
  )
  useEffect(() => { if(id!=null)
    getcultivators()
  },
    [id]
  )


  return (
    <>
      <div className='bg'>
        
        <Title />
        
        <Navbar />
        
        <Para />
        
        <div className='button'>
          <DropDown data={data} findid={setId} companyid={id}/>
        </div>
      
        <Table tabledata={tabledata} />
        <Footer />
      </div>
      
      
    </>
  )
}

export default App
