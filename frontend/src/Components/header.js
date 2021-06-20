import './button.css'
import HeaderButton from './HeaderButton'


function Header (){
    return(
        <header style = {{backgroundColor:'black', color:'white', minWidth: 1080}}>
            <h1>This is my very first react app ever! EVER!!!</h1>
            <p>I am the best at everything right now I am working in the office on this very important project. that makes me feel things you know...</p>
            <HeaderButton /> <HeaderButton /> <HeaderButton />
        </header>
    );
}

export default Header;