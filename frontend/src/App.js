import { useState, useEffect } from "react";
import axios from "axios";
import AccountList from "./Components/AccountList";
import Header from "./Components/header";

function App() {
  const [data, setData] = useState({});
  const getData = () => {
    axios.get("http://localhost:8000/users/").then((res) => {
      console.log('fetched');
      setData(res.data);
    });
  };
  useEffect(() => {
    getData();
  }, []);

  return (
    <div className="App">
      <Header />
      <h1 className="body">
        {data[0] ? <>{data[0].email}</> : <>Loading...</>}
      </h1>
    </div>
  );
}

export default App;
