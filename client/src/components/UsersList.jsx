import UserCards from "./UserCards"

function UsersList({users}){
return(

<div className="grid grid-cols-3 gap-4">


{
    users.map(users =>(
       <UserCards users={users} key={users._id} />

    ))
  }
</div>


)


}
export default UsersList