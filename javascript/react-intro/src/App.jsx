import Greeting from "./greeting"

function App() {
  return (
  <>
  <h1>Hello</h1>
  <Greeting foo = "bar" name= "Imogen" age = {26}/>
  <Greeting name = "Jess" />
  <Greeting />
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium alias cum nostrum ut reprehenderit impedit minima sed corrupti, nisi fugiat distinctio nam ex numquam dicta voluptatum, laudantium deleniti eligendi provident? </p>
  </> 
  )
}


export default App
