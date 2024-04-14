import { useState, useEffect } from "react";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";

function FormPage() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const params = useParams();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      if (!params.id) {
        const res = await axios.post("http://127.0.0.1:8000/api/users", {
          name,
          email,
        });

        console.log(res);
      } else {
        const res = await axios.put(
          `http://127.0.0.1:8000/api/users/${params.id}`,
          {
            name,
            email,
          }
        );
        navigate("/");
      }
    } catch (error) {
      console.log(error);
    }

    e.target.reset();
  };

  useEffect(() => {
    if (params.id) {
      fetchUser();
    }

    async function fetchUser() {
      const res = await axios.get(
        "http://127.0.0.1:8000/api/users/" + params.id
      );
      console.log(res);
      setName(res.data.name);
      setEmail(res.data.email);
    }
  }, []);

  return (
    <div className="flex items-center justify-center h [calc(100vh 10rem)] ">
      <div>
        <form className="bg-zinc-950 p-10 py-20" onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="name"
            className="block py-2 px-3 "
            onChange={(e) => setName(e.target.value)}
            value={name}
            autoFocus
          ></input>

          <input
            type="text"
            placeholder="email"
            className="block py-2 px-3 "
            onChange={(e) => setEmail(e.target.value)}
            value={email}
          ></input>
          <button> {params.id ? "Update user" : "Create user"} </button>
        </form>
{params.id && (
   <button
   className="bg-red-500 hover:bg-red-400 text-white font-bold py-2 rounded mt-5 px-4 "
   onClick={async () => {
     try {
       const res = await axios.delete(
         `http://127.0.0.1:8000/api/users/${params.id}`
       );
       console.log(res);
       navigate("/");
     } catch (error) {
       console.log(error);
     }
   }}
 >
   Delete
 </button>
)}
       
      </div>
    </div>
  );
}
export default FormPage;
