import Navi from "./components/navbar/Navbar";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/home/Home";
import Main from "./pages/main/Main";
import ProductDetails from "./pages/product/ProductDetails";
import OfferForProduct from "./pages/product/OfferForProduct";
import Login from "./pages/login/Login";
import Register from "./pages/register/Register";
import Dashboard from "./pages/dashboard/Dashboard";
import AddProduct from "./pages/product/AddProduct";
import UpdateProduct from "./pages/product/UpdateProduct";
import { ToastContainer } from "react-toastify";
import UpdateUser from "./components/profile/UpdateUser";
import Profile from "./pages/profile/Profile";
import Page404 from "./pages/page404/Page404";
import Payment from "./pages/product/Payment";
import Footer from "./components/footer/Footer";
import { useNaviContext } from "./context/NaviContext";

export default function App() {
  const { visible, setVisible } = useNaviContext();

  const handleVisible = () => {
    setVisible(false);
  };

  return (
    <>
      <div className="font-poppins bg-gray-100 min-h-screen flex flex-col justify-between dark:bg-gray-700">
        <div>
          <Navi />
          <div
            className="py-4 dark:bg-gray-700 dark:text-white"
            onClick={handleVisible}
          >
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/main/*" element={<Main />} />
              <Route path="/productDetails/:id" element={<ProductDetails />} />
              <Route
                path="/offerForProduct/:id"
                element={<OfferForProduct />}
              />
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/payment/product/:productId" element={<Payment />} />
              <Route path="/payment/offer/:offerId" element={<Payment />} />
              <Route path="/dashboard/*" element={<Dashboard />} />
              <Route path="/addProduct" element={<AddProduct />} />
              <Route path="/updateProduct/:id" element={<UpdateProduct />} />
              <Route path="/updateUser/:id" element={<UpdateUser />} />
              <Route path="/profile/*" element={<Profile />} />
              <Route path="*" element={<Page404 />} />
            </Routes>
          </div>
        </div>
        <div>
          <Footer />
        </div>
      </div>
      <ToastContainer
        position="bottom-right"
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />
    </>
  );
}
