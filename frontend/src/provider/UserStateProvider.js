import { createContext, useContext, useState } from "react";

const UserContext = createContext();

export const useUserContext = () => useContext(UserContext);

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState({
    name: null,
    email: null,
    picture_url: null,
  });

  const handleUserChange = (user) => {
    setUser(user);
  };

  return (
    <UserContext.Provider value={{ user, handleUserChange }}>
      {children}
    </UserContext.Provider>
  );
};
