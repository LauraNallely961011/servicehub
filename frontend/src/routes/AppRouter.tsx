// React Router components used to define application routes.
import { BrowserRouter, Route, Routes } from "react-router-dom"

// Application pages.
import HomePage from "../pages/HomePage"
import LoginPage from "../pages/LoginPage"
import DashboardPage from "../pages/DashboardPage"


// Central routing configuration for ServiceHub.
//
// BrowserRouter enables client-side navigation without
// reloading the entire browser page.
function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>

        {/* Public landing page */}
        <Route
          path="/"
          element={<HomePage />}
        />

        {/* Authentication page */}
        <Route
          path="/login"
          element={<LoginPage />}
        />

        {/* Main operational dashboard */}
        <Route
          path="/dashboard"
          element={<DashboardPage />}
        />

      </Routes>
    </BrowserRouter>
  )
}

export default AppRouter