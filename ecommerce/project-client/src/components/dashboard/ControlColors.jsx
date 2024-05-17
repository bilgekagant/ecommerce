import React, { useEffect } from "react";
import { useFormik } from "formik";
import { useColorContext } from "../../context/ColorContext";
import {
  deleteColor,
  getColors,
  postColor,
  updateColor,
} from "../../services/colorService";
import { toast } from "react-toastify";
import { ControlSchema } from "../../validations/controlSchema";
import { useSubmitContext } from "../../context/SubmitContext";

function Controlcolors() {
  const {
    colors,
    setColors,
    selectedColor,
    setSelectedColor,
    updateColorStatus,
    setUpdateColorStatus,
  } = useColorContext();
  const { isSubmitting, setIsSubmitting } = useSubmitContext();
  useEffect(() => {
    setIsSubmitting(false);
    getColors().then((result) => setColors(result.data));
    setUpdateColorStatus(false);
  }, []);

  const { handleSubmit, handleChange, handleBlur, values, errors, touched } =
    useFormik({
      initialValues: {
        name: "",
      },
      onSubmit: (values) => {
        setIsSubmitting(true);
        if (!updateColorStatus) {
          values = { name: capitalize(values.name) };

          postColor(values)
            .then((response) => {
              if (response.success) {
                toast.success(response.message);
                setIsSubmitting(false);
                getColors().then((result) => setColors(result.data));
                values.name = "";
              }
            })
            .catch((err) => {
              toast.error(err.response.data.message);
              setIsSubmitting(false);
            });
        } else {
          const data = {
            colorId: selectedColor.colorId,
            name: capitalize(values.name),
          };
          updateColor(data)
            .then((response) => {
              if (response.success) {
                toast.success(response.message);

                getColors().then((result) => setColors(result.data));
                values.name = "";
                setUpdateColorStatus(false);
              }
              setIsSubmitting(false);
            })
            .catch((err) => {
              toast.error(err.response.data.message);
              setIsSubmitting(false);
            });
        }
      },
      validationSchema: ControlSchema,
    });

  const handleDeleteColor = (colorId) => {
    values.name = "";
    deleteColor(colorId)
      .then((response) => {
        if (response.success) {
          toast.success(response.message);
          getColors().then((result) => setColors(result.data));
        }
        setIsSubmitting(false);
      })
      .catch((err) => {
        console.log(err);
        setIsSubmitting(false);
      });
  };

  const handleUpdateColor = (colorId, colorName) => {
    if (!updateColorStatus) {
      values.name = colorName;
    } else {
      values.name = "";
    }
    setUpdateColorStatus(!updateColorStatus);
    const color = {
      colorId: colorId,
      name: colorName,
    };
    setSelectedColor(color);
  };

  const capitalize = (str) => {
    return str.charAt(0).toUpperCase() + str.slice(1);
  };

  return (
    <div className="flex flex-col md:flex-row md:justify-between items-center pt-16 lg:pb-16 md:px-16">
      <div className="w-full sm:w-2/3 md:w-1/3  mx-auto  bg-white dark:bg-gray-800 rounded-md shadow-item px-4 py-5 order-2 md:order-1">
        <div className="flex flex-col gap-2">
          {colors.map((color) => (
            <div
              className="py-2 px-3 bg-gold text-black rounded text-center flex justify-between items-center"
              key={color.colorId}
            >
              <div>{color.name}</div>
              <div className="flex">
                {updateColorStatus ? (
                  <button
                    onClick={() => handleUpdateColor(color.colorId, color.name)}
                    className={`bg-indigo-500 text-white  px-2 flex items-center justify-center rounded cursor-pointer mr-2 ${
                      isSubmitting ? "submitting" : ""
                    }`}
                    disabled={isSubmitting}
                  >
                    Düzenlemeyi Sonlandır
                  </button>
                ) : (
                  <button
                    onClick={() => handleUpdateColor(color.colorId, color.name)}
                    className={`bg-blue-500 text-white px-2 flex items-center justify-center rounded cursor-pointer mr-2 ${
                      isSubmitting ? "submitting" : ""
                    }`}
                    disabled={isSubmitting}
                  >
                    Düzenle
                  </button>
                )}

                <button
                  onClick={() => handleDeleteColor(color.colorId, color.name)}
                  className={`bg-red-500 text-white w-7 h-7 flex items-center justify-center rounded cursor-pointer ${
                    isSubmitting ? "submitting" : ""
                  }`}
                  disabled={isSubmitting}
                >
                  &#215;
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="w-full sm:w-2/3 md:w-1/2 mx-auto mb-16  py-10 shadow-item  bg-white dark:bg-gray-800 dark:text-white order-1 md:order-2">
        <div className="w-3/4 m-auto">
          <h1 className="font-extrabold text-3xl mb-5 text-center">
            {updateColorStatus ? "Renk Güncelle" : "Renk Ekle"}
          </h1>
          <form onSubmit={handleSubmit}>
            <div className="w-full flex  flex-col bg-darkBlue text-gray-100  px-14 py-14 text-lg">
              <input
                value={values.name}
                onChange={handleChange}
                onBlur={handleBlur}
                name="name"
                type="text"
                className={`text-darkBlue py-2 px-4 w-full ${
                  isSubmitting ? "submitting" : ""
                }`}
                disabled={isSubmitting}
                placeholder="Renk"
                required
              />
              {errors.name && touched.name && (
                <div className="text-red-400 my-2 text-sm">{errors.name}</div>
              )}
            </div>
            <div className="text-right mt-5">
              {updateColorStatus ? (
                <button
                  type="submit"
                  className={`btn  text-lg ${isSubmitting ? "submitting" : ""}`}
                  disabled={isSubmitting}
                >
                  Güncelle
                </button>
              ) : (
                <button
                  type="submit"
                  className={`btn text-lg ${isSubmitting ? "submitting" : ""}`}
                  disabled={isSubmitting}
                >
                  Ekle
                </button>
              )}
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Controlcolors;
