import './footer.css'
import { SlSocialLinkedin } from "react-icons/sl";
import { TiSocialYoutube } from "react-icons/ti";
import { TiSocialTwitter } from "react-icons/ti";


const Footer = () => {
    return (
        <footer >
            <div class='footer'>
        <div className='left'>
            <span><SlSocialLinkedin /></span>
            <span><TiSocialYoutube /></span>
            <span><TiSocialTwitter /></span>

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