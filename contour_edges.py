import cv2
import numpy as np



 # green contour with dual side by side overlay onto one black background window
def contour_edges_wo_overlay_SidebySide(input_path,input_path2):
    # Load the input image
    image = cv2.imread(input_path)
    image2 = cv2.imread(input_path2)

    if image is None:
        raise FileNotFoundError(f"Image '{input_path}' not found.")
    if image2 is None:
        raise FileNotFoundError(f"Image '{input_path2}' not found.")
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    blurred2 = cv2.GaussianBlur(gray2, (5, 5), 0)

    # Detect edges using Canny edge detector
    # Adjust thresholds to keep only major edges
    edges = cv2.Canny(blurred, threshold1=80, threshold2=200)
    edges2 = cv2.Canny(blurred2, threshold1=80, threshold2=200)

    # Find contours (include nested contours with RETR_TREE)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2, hierarchy2 = cv2.findContours(edges2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small contours (to keep only major ones)
    major_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 25]  # 500 is a threshold, adjust as needed
    major_contours2 = [cnt for cnt in contours2 if cv2.contourArea(cnt) > 25]  # 500 is a threshold, adjust as needed

    # Draw major contours on a blank image
    contour_image = np.zeros_like(image)
    contour_image2 = np.zeros_like(image2)

    cv2.drawContours(contour_image, major_contours, -1, (0, 255, 0), 2)
    cv2.drawContours(contour_image2, major_contours2, -1, (0, 255, 0), 2)

    # Resize both images to the same height for proper stacking
    h1, w1 = contour_image.shape[:2]
    h2, w2 = contour_image2.shape[:2]
    max_height = max(h1, h2)
    
    def resize_to_height(img, target_height):
        h, w = img.shape[:2]
        scale = target_height / h
        new_w = int(w * scale)
        return cv2.resize(img, (new_w, target_height))
    
    contour_image_resized = resize_to_height(contour_image, max_height)
    contour_image2_resized = resize_to_height(contour_image2, max_height)

    # Stack images horizontally
    combined = np.hstack((contour_image_resized, contour_image2_resized))

    # Show combined result
    cv2.imshow('Contours Side by Side', combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally save combined image
    cv2.imwrite('major_contours_side_by_side.png', combined)


# green thick overlay onto black background window 
def contour_edges_wo_overlay(input_path):
    # Load the input image
    image = cv2.imread(input_path)

    if image is None:
        raise FileNotFoundError(f"Image '{input_path}' not found.")

    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges using Canny edge detector
    # Adjust thresholds to keep only major edges
    edges = cv2.Canny(blurred, threshold1=80, threshold2=200)

    # Find contours (include nested contours with RETR_TREE)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small contours (to keep only major ones)
    major_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 25]  # 500 is a threshold, adjust as needed

    # Draw major contours on a blank image
    contour_image = np.zeros_like(image)

    cv2.drawContours(contour_image, major_contours, -1, (0, 255, 0), 2)

    # Show the result
    cv2.imshow('Major Contours', contour_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally, save the result
    cv2.imwrite('major_contours.png', contour_image)
    return contour_image

# green thick overlay onto image background  
def contour_edges_w_overlay(input_path):

    image = cv2.imread(input_path)
    if image is None:
        raise FileNotFoundError("Image 'reference_part.png' not found.")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise but keep edges
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detection to capture intensity differences
    edges = cv2.Canny(blurred, threshold1=80, threshold2=200)

    # Find contours (include nested contours with RETR_TREE)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Optional: filter very tiny contours but keep nested ones
    major_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 500]  # adjust threshold as needed

    # Overlay contours on the original image
    overlay_image = image.copy()
    cv2.drawContours(overlay_image, major_contours, -1, (0, 0, 255), 2)

    # Show results
    cv2.imshow('Major Nested Contours Overlay', overlay_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the result
    cv2.imwrite('major_nested_contours_overlay.png', overlay_image)
    return overlay_image



#################################################################################
#################################################################################
#               belwo are used functions, above functions are not used 
#################################################################################
#################################################################################
def img_mask_contour_comparison(image1_path,image2_path):


    # Load the two input images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)  # your second image

    if image1 is None or image2 is None:
        raise FileNotFoundError("One or both input images not found.")

    # Resize images to match (optional if same size)
    if image1.shape != image2.shape:
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Convert to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)



    # Blur to reduce noise
    blur1 = cv2.GaussianBlur(gray1, (5, 5), 0)
    blur2 = cv2.GaussianBlur(gray2, (5, 5), 0)

    # Canny edge detection (captures intensity differences)
    edges1 = cv2.Canny(blur1, 50, 150)
    edges2 = cv2.Canny(blur2, 50, 150)

    # Find contours including nested ones
    contours1, _ = cv2.findContours(edges1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(edges2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Create blank masks
    mask1 = np.zeros_like(gray1)
    mask2 = np.zeros_like(gray2)

    # Draw contours as filled shapes
    cv2.drawContours(mask1, contours1, -1, 255, thickness=cv2.FILLED)
    cv2.drawContours(mask2, contours2, -1, 255, thickness=cv2.FILLED)

    # Compute absolute difference between masks
    diff_mask = cv2.absdiff(mask1, mask2)

    # Highlight differences on the original image (image2)
    highlighted = image2.copy()
    highlighted[diff_mask > 0] = [0, 0, 255]  # red differences



            ## Resize both images to the same height for proper stacking
            #h1, w1 = mask1.shape[:2]
            #h2, w2 = mask2.shape[:2]
            #max_height = max(h1, h2)
            #def resize_to_height(img, target_height):
            #    h, w = img.shape[:2]
            #    scale = target_height / h
            #    new_w = int(w * scale)
            #    return cv2.resize(img, (new_w, target_height))
            #contour_image_resized = resize_to_height(mask1, max_height)
            #contour_image2_resized = resize_to_height(mask2, max_height)
            ## Stack images horizontally
            #combined = np.hstack((contour_image_resized, contour_image2_resized))

            ## Show combined result
            #cv2.imshow('contour_comparison Side by Side', combined)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            ## Save result
            #cv2.imwrite('contour_comparison.png', combined)


   # # Show results
   # cv2.imshow('Contour Differences', highlighted)
   # cv2.waitKey(0)
   # cv2.destroyAllWindows()

    # Save result
    #cv2.imwrite('contour_differences.png', highlighted)
    return mask1 ,mask2




def img_mask_contour_comparisonV2(image1_path, image2_path):

    # Load images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    if image1 is None or image2 is None:
        raise FileNotFoundError("One or both input images not found.")

    # Convert to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # -----------------------------
    # ORB FEATURE ALIGNMENT
    # -----------------------------
    orb = cv2.ORB_create(5000)

    kp1, des1 = orb.detectAndCompute(gray1, None)
    kp2, des2 = orb.detectAndCompute(gray2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # Use best matches
    good_matches = matches[:100]

    pts1 = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1,1,2)
    pts2 = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1,1,2)

    # Compute homography
    H, mask = cv2.findHomography(pts2, pts1, cv2.RANSAC, 5.0)

    # Warp image2 to image1 perspective
    aligned_image2 = cv2.warpPerspective(image2, H, (image1.shape[1], image1.shape[0]))

    # -----------------------------
    # Continue with your pipeline
    # -----------------------------

    gray2_aligned = cv2.cvtColor(aligned_image2, cv2.COLOR_BGR2GRAY)

    blur1 = cv2.GaussianBlur(gray1, (5,5), 0)
    blur2 = cv2.GaussianBlur(gray2_aligned, (5,5), 0)

    edges1 = cv2.Canny(blur1, 50, 150)
    edges2 = cv2.Canny(blur2, 50, 150)

    contours1, _ = cv2.findContours(edges1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(edges2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    mask1 = np.zeros_like(gray1)
    mask2 = np.zeros_like(gray1)

    cv2.drawContours(mask1, contours1, -1, 255, thickness=cv2.FILLED)
    cv2.drawContours(mask2, contours2, -1, 255, thickness=cv2.FILLED)

    diff_mask = cv2.absdiff(mask1, mask2)

    # Highlight differences
    highlighted = aligned_image2.copy()
    highlighted[diff_mask > 0] = [0,0,255]
    #cv2.imshow("highlighted", highlighted)
    #cv2.imshow("mask 1", mask1)
    #cv2.imshow("mask 2", mask2)

    return  highlighted, mask1, mask2

def detect_differences(img1, img2,
                       min_contour_area=500,
                       blur_size=5,
                       threshold=100):

    # Convert to grayscale
    g1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    g2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # --- FEATURE ALIGNMENT (rotation/scale/translation robust) ---
    orb = cv2.ORB_create(5000)

    k1, d1 = orb.detectAndCompute(g1, None)
    k2, d2 = orb.detectAndCompute(g2, None)

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(d1, d2)

    matches = sorted(matches, key=lambda x: x.distance)

    pts1 = np.float32([k1[m.queryIdx].pt for m in matches]).reshape(-1,1,2)
    pts2 = np.float32([k2[m.trainIdx].pt for m in matches]).reshape(-1,1,2)

    # Homography alignment
    H, mask = cv2.findHomography(pts2, pts1, cv2.RANSAC, 5.0)

    aligned_img2 = cv2.warpPerspective(img2, H, (img1.shape[1], img1.shape[0]))

    g2_aligned = cv2.cvtColor(aligned_img2, cv2.COLOR_BGR2GRAY)

    # --- NOISE REDUCTION ---
    g1_blur = cv2.GaussianBlur(g1, (blur_size, blur_size), 0)
    g2_blur = cv2.GaussianBlur(g2_aligned, (blur_size, blur_size), 0)

    # --- DIFFERENCE IMAGE ---
    diff = cv2.absdiff(g1_blur, g2_blur)

    _, thresh = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # --- MORPH CLEANUP ---
    kernel = np.ones((5,5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    thresh = cv2.dilate(thresh, kernel, iterations=2)

    # --- FIND DIFFERENCE REGIONS ---
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    result = aligned_img2.copy()

    for c in contours:
        area = cv2.contourArea(c)

        if area > min_contour_area:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(result,(x,y),(x+w,y+h),(0,0,255),2)

    return result, thresh

def add_label(image, text):

    # Convert grayscale to BGR if needed
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    img = image.copy()

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.8
    thickness = 2
    color = (255,255,0)

    # background rectangle
    (w, h), _ = cv2.getTextSize(text, font, font_scale, thickness)
    cv2.rectangle(img, (5,5), (w+15, h+15), (0,0,0), -1)

    # draw label
    cv2.putText(img, text, (10, h+10), font, font_scale, color, thickness)

    return img

def display_horizontally(images, images_row2=None, window_name="Images", window_size=(1920,1080), save_path=None):

    if len(images) == 0:
        raise ValueError("No images provided")

    def process_row(img_list):
        processed = []

        # Convert grayscale to BGR
        for img in img_list:
            if len(img.shape) == 2:
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            processed.append(img)

        # Match heights
        max_height = max(img.shape[0] for img in processed)

        resized = []
        for img in processed:
            h, w = img.shape[:2]
            scale = max_height / h
            new_w = int(w * scale)
            resized.append(cv2.resize(img, (new_w, max_height)))

        return np.hstack(resized)

    # Build first row
    row1 = process_row(images)

    # Build second row if provided
    if images_row2 is not None and len(images_row2) > 0:
        row2 = process_row(images_row2)

        # Pad rows to equal width
        max_w = max(row1.shape[1], row2.shape[1])

        def pad_width(img):
            h, w = img.shape[:2]
            if w < max_w:
                pad = np.zeros((h, max_w - w, 3), dtype=np.uint8)
                img = np.hstack([img, pad])
            return img

        row1 = pad_width(row1)
        row2 = pad_width(row2)

        combined = np.vstack([row1, row2])

    else:
        combined = row1

    # ----- Fit to window while preserving aspect ratio -----
    win_w, win_h = window_size
    h, w = combined.shape[:2]

    scale = min(win_w / w, win_h / h)

    new_w = int(w * scale)
    new_h = int(h * scale)

    scaled = cv2.resize(combined, (new_w, new_h))

    # ----- Create black canvas -----
    canvas = np.zeros((win_h, win_w, 3), dtype=np.uint8)

    x_offset = (win_w - new_w) // 2
    y_offset = (win_h - new_h) // 2

    canvas[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = scaled

    # ----- Display -----
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, win_w, win_h)
    cv2.imshow(window_name, canvas)

    if save_path is not None:
        cv2.imwrite(save_path, combined)

    return combined

if __name__ == "__main__":
 

   highlighted,ref_contour,test_contour = img_mask_contour_comparisonV2("reference_part.png", "test_part.png")
   ref_contour = cv2.cvtColor(ref_contour, cv2.COLOR_GRAY2BGR)
   test_contour = cv2.cvtColor(test_contour, cv2.COLOR_GRAY2BGR)
   result, diffmask = detect_differences(ref_contour, test_contour)

   
   # Add labels
   high_img = add_label(highlighted, "Part Highlights")
   ref_img  = add_label(ref_contour, "Reference Mask Outline")
   part_img = add_label(test_contour, "Part Masking Outline")
   mask_img = add_label(diffmask, "Masking Differences")
   anno_img = add_label(result, "Annotations")        
   
   images = [

        ref_img,
        high_img,
        part_img,
        mask_img,
        anno_img
    ]



    # Load original and part being compared images
   ref_img = cv2.imread("reference_part.png")
   part_being_compared = cv2.imread("test_part.png")
   if ref_img is None or part_being_compared is None:
       raise FileNotFoundError("One or both input images not found.")
    # annotate the images to destinguish them
   ref_img = add_label(ref_img, "Reference Image")
   part_being_compared = add_label(highlighted, "Part being compared")
    # make a list to pass into display function
   ref_and_og_img = [
       ref_img,
       part_being_compared
   ]   


   display_horizontally(images, images_row2 = ref_and_og_img)



   cv2.waitKey(0)
   cv2.destroyAllWindows()