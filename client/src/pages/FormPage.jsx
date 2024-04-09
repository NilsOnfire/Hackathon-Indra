import { Form } from "react-router-dom";

function FormPage() {
  return (
    <div>
      <form>
        <input type="text" placeholder="name"
        className="block py-2 px-3 "
        ></input>
        <button>save</button>
      </form>
    </div>
  );
}
export default FormPage;
