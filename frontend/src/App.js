import AccountList from './Components/AccountList'
import Header from './Components/header'

function App() {
  return (
    <div className="App">
        <Header />
        <div className="body">
          <code>
            This is my code
          </code>
          <AccountList />
        </div>
        
    </div>
  );
}

export default App;