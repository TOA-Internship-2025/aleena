import './footer.css'
import { BsLinkedin } from "react-icons/bs";
import { BsYoutube } from "react-icons/bs";
import { BsTwitterX } from "react-icons/bs";
import { FaInstagram } from "react-icons/fa6";

const Footer = () => {
    return (
        <footer >
            <div class='footer'>
        <div className='left'>
     <span><BsTwitterX /></span>
<span><FaInstagram /></span>
            <span><BsYoutube /></span>
            <span><BsLinkedin /></span>

        </div>
        <div className='middle'>

            <h4>Partners</h4>
            <span><a href="#home">XYZ</a></span>
            <span><a href="#find">GrowM</a></span>
   
        </div>
       <div className='right'>
       <h4>Resources</h4>
            <span><a href="#home">Blog</a></span>
            <span><a href="#find">Support</a></span>
            <span><a href="#about">Contact Us</a></span>
        </div>
    </div>
    </footer>
    )
}
export default Footer