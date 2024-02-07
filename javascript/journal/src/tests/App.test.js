import { render } from "@testing-library/react"
import { describe, it } from "vitest"
import App from "../components/App"

describe('App Component', () => {
  it('renders the Home component', () => {
    render(
      <App />
    )
    
  })
})