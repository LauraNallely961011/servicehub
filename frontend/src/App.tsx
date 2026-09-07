// Main application router.
//
// Keeping the routing logic in a separate component
// helps keep App.tsx simple and scalable.
import AppRouter from "./routes/AppRouter"


// Root component of the ServiceHub frontend.
function App() {
  return <AppRouter />
}

export default App