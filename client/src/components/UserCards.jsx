import { useNavigate } from "react-router-dom";

function UserCards({ users }) {
  const navigate = useNavigate();

  return (
    <div
      className="bg-zinc-950 p-4 rounded-lg hover:cursor-pointer hover:bg-gray-950"
      onClick={() => {
        navigate(`/user/${users._id}`);
      }}
    >
      <h2 className="text-2xl font-bold">{users.name}</h2>
      <p className="text-gray-700">Email: {users.email}</p>
      <p className="text-gray-700">Cellphone: {users.cellphone}</p>
      <p className="text-gray-700">Birthday: {users.birthday}</p>
      <p className="text-gray-700">Gender: {users.gender}</p>
      <p className="text-gray-700">
        Professional Profile: {users.professionalProfile}
      </p>
      <p className="text-gray-700">Address: {users.address}</p>
      <p className="text-gray-700">City: {users.city}</p>
      <p className="text-gray-700">State: {users.state}</p>
      <p className="text-gray-700">Postal Code: {users.postalCode}</p>
      <p className="text-gray-700">
        Link Profile Photo: {users.linkProfilePhoto}
      </p>
      <p className="text-gray-700">Type Profile: {users.typeProfile}</p>

      <h3 className="text-xl font-bold">Applications:</h3>
      <ul>
        {users.applications &&
          users.applications.map((application, index) => (
            <li key={index}>
              Vacancy: {application.vacancy}, Status: {application.status}, Date
              Applied: {application.date_applied}
            </li>
          ))}
      </ul>

      <h3 className="text-xl font-bold">Processes:</h3>
      <ul>
        {users.processes &&
          users.processes.map((process, index) => (
            <li key={index}>
              Date: {process.date}, Job: {process.job}, Description:{" "}
              {process.description}
              <ul>
                {process.stages &&
                  process.stages.map((stage, stageIndex) => (
                    <li key={stageIndex}>
                      Stage {stageIndex + 1}: {stage.title}, Date: {stage.date},
                      Description: {stage.description}
                    </li>
                  ))}
              </ul>
            </li>
          ))}
      </ul>
    </div>
  );
}
export default UserCards;
