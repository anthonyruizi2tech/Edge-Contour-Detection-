import os 
import cv2

def open_full_res_camera(cam_index=0):
    cap = cv2.VideoCapture(cam_index, cv2.CAP_DSHOW)  # CAP_DSHOW helps on Windows

    if not cap.isOpened():
        raise RuntimeError("Could not open webcam.")

    # Try setting very high resolution (camera will clamp to max supported)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)

    # Get actual resolution after setting
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"[INFO] Camera initialized at: {width} x {height}")

    return cap



def call_capture_feed():
    cap = open_full_res_camera()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Get resolution per frame (some cameras can dynamically change)
        h, w = frame.shape[:2]
        print(f"Frame Resolution: {w} x {h}")

        # Display
        cv2.imshow("Webcam Feed (Full Resolution)", frame)

        # Exit on 'q' or capture on 'c'
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            cv2.imwrite('output_frame.png', frame)
            print("Image saved as output_frame.png")
            break

    cap.release()
    cv2.destroyAllWindows()


def verify_path(imag_path):
    # Verify paths exist
    if os.path.isfile(imag_path):
        print(f" Image exists: {imag_path}")
    else:
        print(f" Image NOT found: {imag_path}")
        exit()




def overlay_image_on_feed(frame, overlay_img, opacity=30):
    """Overlay the reference image onto the camera frame with specified opacity, keeping the aspect ratio intact."""
    # Get the dimensions of the frame
    frame_h, frame_w = frame.shape[:2]

    # Get the dimensions of the overlay image
    overlay_h, overlay_w = overlay_img.shape[:2]

    # Resize overlay image to fit within the frame while maintaining aspect ratio
    scale_factor = min(frame_w / overlay_w, frame_h / overlay_h)
    new_overlay_w = int(overlay_w * scale_factor)
    new_overlay_h = int(overlay_h * scale_factor)

    # Resize the overlay image
    resized_overlay = cv2.resize(overlay_img, (new_overlay_w, new_overlay_h))

    # Calculate the position to center the image on the frame
    x_offset = (frame_w - new_overlay_w) // 2
    y_offset = (frame_h - new_overlay_h) // 2

    # Create a region of interest (ROI) for the frame where the overlay will go
    roi = frame[y_offset:y_offset + new_overlay_h, x_offset:x_offset + new_overlay_w]

    # Blend the images using the specified opacity
    alpha = opacity / 100.0
    cv2.addWeighted(resized_overlay, alpha, roi, 1 - alpha, 0, roi)

    return frame

def call_capture_feed_w_opacity(laplacian_ref_img_path = None, opacity=30):
    if laplacian_ref_img_path:
        """Capture webcam feed and overlay an image with specified opacity without stretching it."""
        # Verify the image exists before opening to prevent crashing 
        verify_path(laplacian_ref_img_path)
        
        # Open the reference image for opacity overlay
        lapacian_ref_img = cv2.imread(laplacian_ref_img_path, cv2.IMREAD_COLOR)
        
        if lapacian_ref_img is None:
            print("Error: Unable to load reference image.")
            return

        # Open camera with full resolution
        cap = cv2.VideoCapture(0)  # Assuming 0 is your camera index
        
        if not cap.isOpened():
            print("Error: Camera not opened.")
            return
        
        while True:
            ret, frame = cap.read()  # Retrieve frame
            frame_copy_wo_overlay = frame.copy() #make copy to reatain current frame without opacity

            if not ret:
                print("Failed to grab frame")
                break

            # Overlay the reference image with the specified opacity
            frame_w_overlay = overlay_image_on_feed(frame, lapacian_ref_img, opacity)

            # Get resolution per frame (some cameras can dynamically change)
            h, w = frame_w_overlay.shape[:2]
            print(f"Frame w overlay Resolution: {w} x {h}")

            # Display the webcam feed with overlay
            cv2.imshow("Webcam Feed (Full Resolution)", frame_w_overlay)

            # Exit on 'q' or capture on 'c'
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('c'):
                cv2.imwrite('output_frame.png', frame_copy_wo_overlay)
                print("Image saved as output_frame.png")
                break

        # Release the camera and close windows
        cap.release()
        cv2.destroyAllWindows()
    
    if laplacian_ref_img_path == None:
        cap = open_full_res_camera()

        while True:
            ret, frame = cap.read()

            if not ret:
                print("Failed to grab frame")
                break

            # Get resolution per frame (some cameras can dynamically change)
            h, w = frame.shape[:2]
            print(f"Frame Resolution: {w} x {h}")

            # Display
            cv2.imshow("Webcam Feed (Full Resolution)", frame)

            # Exit on 'q' or capture on 'c'
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('c'):
                cv2.imwrite('output_frame.png', frame)
                print("Image saved as output_frame.png")
                break

        cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":

    #call_capture_feed()


    ref_image_path = 'lapacian_reference_part.png'
    call_capture_feed_w_opacity(ref_image_path)
    #call_capture_feed_w_opacity()
