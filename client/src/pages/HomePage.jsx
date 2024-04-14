import { useEffect, useState } from "react";
import axios from "axios";
import UsersList from "../components/UsersList";

function HomePage() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    async function fetchUsers() {
      const res = await axios.get("http://127.0.0.1:8000/api/users");
      setUsers(res.data);
    }

    fetchUsers();
  }, []);

  return (
    <>
      <h1 className="text-3xl font-bold">Home page</h1>
      <UsersList users={users} />
    </>
  );
}
export default HomePage;
