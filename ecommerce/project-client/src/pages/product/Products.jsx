import React, { useEffect, useState } from "react";
import {
  getProducts,
  getProductsByBrand,
  getProductsByCategory,
  getProductsByColor,
  getProductsByUsingState,
} from "../../services/productService";
import { NavLink, useParams } from "react-router-dom";
import defaultImage from "../../assets/default.png";
import { useProductContext } from "../../context/ProductContext";
import { getProductsByOwner } from "../../services/productService";
import { useAuthContext } from "../../context/AuthContext";

function Products() {
  const { products, setProducts } = useProductContext();
  const { brandId, colorId, categoryId, ownerId, usingStateId } = useParams();
  const { isLogged } = useAuthContext();

  const apiImagesUrl = "https://localhost:7153/uploads/images/";

  useEffect(() => {
    if (brandId) {
      getProductsByBrand(brandId).then((result) => setProducts(result.data));
    } else if (colorId) {
      getProductsByColor(colorId).then((result) => setProducts(result.data));
    } else if (usingStateId) {
      getProductsByUsingState(usingStateId).then((result) =>
        setProducts(result.data)
      );
    } else if (categoryId) {
      getProductsByCategory(categoryId).then((result) =>
        setProducts(result.data)
      );
    } else if (ownerId) {
      getProductsByOwner(ownerId).then((result) => setProducts(result.data));
    } else {
      getProducts().then((result) => setProducts(result.data));
    }
  }, [brandId, colorId, categoryId, ownerId, usingStateId]);

  return (
    <div className="bg-gray-100 dark:bg-gray-700">
      <div className="grid grid-cols-12 gap-x-8 gap-y-10 sm:gap-y-10 md:gap-y-20">
        {products.map((product, index) => (
          <NavLink
            key={index}
            className="flex flex-col justify-between rounded-md h-full  shadow-item mb-10 dark:bg-darkBlue dark:text-white col-span-12 sm:col-span-6 md:col-span-4 lg:col-span-3"
            to={isLogged ? `/productdetails/${product.productId}` : "/login"}
          >
            <img
              src={
                product.imagePath
                  ? apiImagesUrl + product.imagePath
                  : defaultImage
              }
              className="rounded-t-md h-2/3 object-cover object-center w-full flex-shrink-0"
              alt=""
            />
            <div className="text-center bg-white dark:bg-gray-800 flex flex-col h-full justify-between py-3 px-5">
              <div className="flex justify-between">
                <p>Ürün</p>
                <p>{product.productName}</p>
              </div>
              <div className="flex justify-between">
                <p>Kategori</p>
                <p>{product.categoryName}</p>
              </div>
              {product.brandName && (
                <div className="flex justify-between">
                  <p>Marka</p>
                  <p>{product.brandName}</p>
                </div>
              )}
              {product.colorName && (
                <div className="flex justify-between">
                  <p>Renk</p>
                  <p>{product.colorName}</p>
                </div>
              )}
              <div className="flex justify-between">
                <p>Fiyat</p>
                <p>{product.price}₺</p>
              </div>
            </div>

            <div>
              {product.isOfferable ? (
                <div className="py-1 bg-teal-500 text-white text-center text-sm">
                  Teklif Verilebilir
                </div>
              ) : (
                <div className="py-1 bg-indigo-500  text-white text-center text-sm">
                  Teklif Verilemez
                </div>
              )}

              {product.isSold ? (
                <div className="py-1 bg-rose-500 rounded-b text-white text-center text-sm ">
                  Satıldı
                </div>
              ) : (
                <div className="py-1 bg-lime-500 rounded-b text-white text-center text-sm">
                  Satılmadı
                </div>
              )}
            </div>
          </NavLink>
        ))}
      </div>
    </div>
  );
}

export default Products;
