import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
from rembg import remove
import os 

#rembg with canny edge detection. this is obsolete to lapacian due to incresed false edge detection
def rem_bg_canny(image_path):
    # Load the original image
    image_original = cv2.imread(image_path, cv2.IMREAD_COLOR)
    file_basename = os.path.splitext(os.path.basename(image_path))[0]

    # Convert the image to bytes for rembg to process
    _, img_bytes = cv2.imencode('.png', image_original)
    img_bytes = img_bytes.tobytes()

    print(f"rem_bg_canny: removing background on {file_basename}")
    # Use rembg to remove the background
    output_bytes = remove(img_bytes)

    # Convert the output bytes to an image
    nparr = np.frombuffer(output_bytes, np.uint8)
    image_no_bg = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    # Convert to grayscale (ignoring alpha channel if present)
    image_gray = cv2.cvtColor(image_no_bg, cv2.COLOR_BGR2GRAY)

    # Reduce noise using Gaussian blur
    img_blur = cv2.GaussianBlur(image_gray, (3, 3), 0)

    # Apply Canny edge detection
    print(f"rem_bg_canny: applying Canny edge detection on image: {file_basename}")
    edges = cv2.Canny(img_blur, threshold1=50, threshold2=150)

    # Convert images to RGB for correct display in matplotlib
    image_original_rgb = cv2.cvtColor(image_original, cv2.COLOR_BGR2RGB)
    image_no_bg_rgb = cv2.cvtColor(image_no_bg, cv2.COLOR_BGR2RGB)

    # Plot the images
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 15))

    ax1.set_title(f'{file_basename}.png Image')
    ax1.imshow(image_original_rgb)
    ax1.axis('off')

    ax2.set_title('Image with Background Removed')
    ax2.imshow(image_no_bg_rgb)
    ax2.axis('off')

    ax3.set_title('Canny Edge Detection on No Background Image')
    ax3.imshow(edges, cmap='gray')
    ax3.axis('off')

    plt.show()

    return edges

def rem_bg_rgb(image_path):
    # Load the original image
    image_original = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Convert the image to bytes for rembg to process
    _, img_bytes = cv2.imencode('.png', image_original)
    img_bytes = img_bytes.tobytes()

    # Use rembg to remove the background
    output_bytes = remove(img_bytes)

    # Convert the output bytes to an image
    nparr = np.frombuffer(output_bytes, np.uint8)
    image_no_bg = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    # Ensure we have a 3-channel (RGB/BGR) image for display purposes
    if image_no_bg.shape[2] == 4:  # If image has an alpha channel
        image_no_bg = cv2.cvtColor(image_no_bg, cv2.COLOR_BGRA2BGR)

    # Convert images to RGB for correct display in matplotlib (only for showing)
    image_original_rgb = cv2.cvtColor(image_original, cv2.COLOR_BGR2RGB)
    image_no_bg_rgb = cv2.cvtColor(image_no_bg, cv2.COLOR_BGR2RGB)

    # Plot the images
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 15))

    ax1.set_title('Original Image')
    ax1.imshow(image_original_rgb)
    ax1.axis('off')

    ax2.set_title('Image with Background Removed')
    ax2.imshow(image_no_bg_rgb)
    ax2.axis('off')

    plt.show()



    return image_no_bg

#lapacian is ioptimal in this case. better edge detection and reduced false positives to canny. better alignment in ORB as well.
def rem_bg_lapacian(image_path):
    # Load the original image
    image_original = cv2.imread(image_path, cv2.IMREAD_COLOR)
    file_basename  = os.path.splitext(os.path.basename(image_path))[0]

    # Convert the image to bytes for rembg to process
    _, img_bytes = cv2.imencode('.png', image_original)
    img_bytes = img_bytes.tobytes()

    print(f"rem_bg_lapacian: removing background on {file_basename}")
    # Use rembg to remove the background
    output_bytes = remove(img_bytes)

    # Convert the output bytes to an image
    nparr = np.frombuffer(output_bytes, np.uint8)
    image_no_bg = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    # Convert to grayscale (ignoring alpha channel)
    image_gray = cv2.cvtColor(image_no_bg, cv2.COLOR_BGR2GRAY)

    # Reduce noise using Gaussian blur
    img = cv2.GaussianBlur(image_gray, (3, 3), 0)

    # Apply Laplacian filter for edge detection
    print(f"rem_bg_lapacian: applying Lapacian for edge detection on image: {file_basename}")
    filtered_image = cv2.Laplacian(img, ddepth=cv2.CV_16S, ksize=3)

    # Convert the result to uint8
    filtered_image = cv2.convertScaleAbs(filtered_image)

    # Convert images to RGB for correct display in matplotlib
    image_original_rgb = cv2.cvtColor(image_original, cv2.COLOR_BGR2RGB)
    image_no_bg_rgb = cv2.cvtColor(image_no_bg, cv2.COLOR_BGR2RGB)

    # Plot the images
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 15))

    ax1.set_title(f'{file_basename}.png Image')
    ax1.imshow(image_original_rgb)
    ax1.axis('off')

    ax2.set_title('Image with Background Removed')
    ax2.imshow(image_no_bg_rgb)
    ax2.axis('off')

    ax3.set_title('Laplacian Filtered No Background Image')
    ax3.imshow(filtered_image, cmap='gray')
    ax3.axis('off') 


    plt.show()
    return filtered_image


def detect_differences(img1, img2,
                       min_contour_area=50,
                       blur_size=5,
                       threshold=43):


    """
    img1: The reference image (what you want to compare against).

    img2: The test image (what you want to detect differences in).

    min_contour_area: Minimum size (in pixels) for differences to be considered relevant. Smaller differences will be ignored.

    blur_size: Kernel size for Gaussian blur — helps reduce noise.

    threshold: Pixel intensity difference threshold to classify a pixel as “different.”
    """

    print(f"detect_differences: Detecting differences in images...")

    # Convert to grayscale if image is color
    g1 = img1 if len(img1.shape) == 2 else cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    g2 = img2 if len(img2.shape) == 2 else cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

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

    # Convert to grayscale if necessary
    g2_aligned = aligned_img2 if len(aligned_img2.shape) == 2 else cv2.cvtColor(aligned_img2, cv2.COLOR_BGR2GRAY)

    print(f"detect_differences: noise reduction (GaussianBlur blur_size: {blur_size})...")
    # --- NOISE REDUCTION ---
    g1_blur = cv2.GaussianBlur(g1, (blur_size, blur_size), 0)
    g2_blur = cv2.GaussianBlur(g2_aligned, (blur_size, blur_size), 0)

    # --- DIFFERENCE IMAGE ---
    print(f"detect_differences: diff detect with...\n       min_contour_area: {min_contour_area}\n       Thresh: {threshold}\n       blur_size:{blur_size}")
    diff = cv2.absdiff(g1_blur, g2_blur)
    _, thresh = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # --- MORPH CLEANUP ---
    kernel = np.ones((5,5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    thresh = cv2.dilate(thresh, kernel, iterations=2)

    # --- FIND DIFFERENCE REGIONS ---
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    result = aligned_img2.copy()

    # Ensure it is BGR (3 channels) even if input was grayscale
    if len(result.shape) == 2:
        result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
    
    print(f"detect_differences: Contouring Differences: area > min contour area {min_contour_area}") 
    for c in contours:
        area = cv2.contourArea(c)
        if area > min_contour_area:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(result, (x,y), (x+w,y+h), (0,0,255), 2)

    return result, thresh


def cv2_to_rgb(img):
    if len(img.shape) == 3:  # Color image
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img  # Grayscale image remains the same


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


def orb_alignment_detection(ref_img_path,test_img_path):
    print("opening images for ORB alignment and detection")
    # Load the images in grayscale for feature extraction
    ref_img = cv2.imread(ref_img_path, cv2.IMREAD_GRAYSCALE)
    test_img = cv2.imread(test_img_path, cv2.IMREAD_GRAYSCALE)

    # Check if images were loaded correctly
    if ref_img is None:
        print(f"Cannot open reference image: {ref_img_path}")
        sys.exit(1)
    if test_img is None:
        print(f"Cannot open test image: {test_img_path}")
        sys.exit(1)

    print(f"orb_alignment_detection: Initializing orb detetcor for images: \n    REF: {ref_img_path}\n   PART: {test_img_path}")
    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Detect keypoints and descriptors
    kp_ref, des_ref = orb.detectAndCompute(ref_img, None)
    kp_test, des_test = orb.detectAndCompute(test_img, None)

    # Match descriptors using BFMatcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des_ref, des_test)

    # Sort matches by distance (lower distance is better)
    matches = sorted(matches, key=lambda x: x.distance)

    # Use the top N matches for affine transformation estimation
    N = 30
    good_matches = matches[:N]
    print(f"orb_alignment_detection: Using {N} matches for affine transformation estimation.")


    # Extract matched keypoints
    pts_ref = np.float32([kp_ref[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    pts_test = np.float32([kp_test[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # Compute the affine transformation matrix (translation, rotation, scaling)
    # Note: Using RANSAC for robust matching
    M, mask = cv2.estimateAffine2D(pts_test, pts_ref, method=cv2.RANSAC, ransacReprojThreshold=5.0)

    # Apply the affine transformation to align the test image to the reference image
    aligned_img = cv2.warpAffine(test_img, M, (ref_img.shape[1], ref_img.shape[0]))

    # Heatmap of unaligned portions (difference between reference and aligned image)
    diff_img = cv2.absdiff(ref_img, aligned_img)
    heatmap = cv2.applyColorMap(diff_img, cv2.COLORMAP_JET)

    # Convert aligned image to color (3 channels) for overlaying
    aligned_img_color = cv2.cvtColor(aligned_img, cv2.COLOR_GRAY2BGR)

    # Resize aligned_img to match reference image size
    aligned_img_resized = cv2.resize(aligned_img, (ref_img.shape[1], ref_img.shape[0]))

    # Convert to color for overlay
    aligned_img_color = cv2.cvtColor(aligned_img_resized, cv2.COLOR_GRAY2BGR)

    # Overlay the aligned image on top of the reference image
    overlay = cv2.addWeighted(cv2.cvtColor(ref_img, cv2.COLOR_GRAY2BGR), 0.5, aligned_img_color, 0.5, 0)

    # Draw the matches between the two images
    match_img = cv2.drawMatches(ref_img, kp_ref, test_img, kp_test, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)


    # detect differences in test image in relation to reference image, after test part has been aligned
    result, diffmask = detect_differences(ref_img, aligned_img_resized)

    mask_img = add_label(diffmask, "Masking Differences")
    anno_img = add_label(result, "Annotations")  

    print(f"orb_alignment_detection: Displaying annotations with key match points in images...")


    # Display results
    plt.figure(figsize=(15, 7))

    # Top row: Display keypoint matches
    plt.subplot(2, 6, 1)
    plt.imshow(test_img, cmap='gray')
    plt.title('Test Image')

    plt.subplot(2, 6, 2)
    plt.imshow(cv2.drawKeypoints(test_img, kp_test, None, color=(0, 255, 0), flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS))
    plt.title('(Part) Detected Points \nfor Alignment')

    plt.subplot(2, 6, 3)
    plt.imshow(heatmap)
    plt.title('Heat Map of \nUnaligned Portions')

    #plt.subplot(2, 6, 4)
    #plt.imshow(overlay)
    #plt.title('Aligned Images Overlayed')
    plt.subplot(2, 6, 4)
    plt.imshow(aligned_img_color)
    plt.title('Aligned test Image')

    plt.subplot(2, 6, 5)
    plt.imshow(mask_img, cmap= 'gray')
    plt.title('Masking Differences\n(Ref vs test part aligned)')

    plt.subplot(2, 6, 6)
    plt.imshow(cv2_to_rgb(anno_img))
    plt.title('Annotations')


    # Bottom row: Display reference image and matches
    plt.subplot(2, 6, 7)
    plt.imshow(cv2_to_rgb(ref_img), cmap='gray')
    plt.title('Reference Image')

    plt.subplot(2, 6, 8)
    ref_kp_img = cv2.drawKeypoints(cv2.cvtColor(ref_img, cv2.COLOR_GRAY2BGR), kp_ref, None, color=(0, 255, 0), flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
    plt.imshow(cv2_to_rgb(ref_kp_img))
    plt.title('(Ref) Detected Points \nfor Alignment')

    plt.subplot(2, 6, 9)
    plt.imshow(match_img)
    plt.title('Keypoint Matches')

    plt.axis('off')
    plt.tight_layout()
    plt.show()


def verify_path(imag_path):
    # Verify paths exist
    if os.path.isfile(imag_path):
        print(f" Image exists: {imag_path}")
    else:
        print(f" Image NOT found: {imag_path}")
        exit()



#######################################################
#                Main program 
#######################################################
if __name__ == "__main__":


    # Define image paths
    ref_img_path = 'reference_part.png'
    verify_path(ref_img_path)
    ref_imag_basename  = os.path.splitext(os.path.basename(ref_img_path))[0]

    test_img_path = 'test_part.png'
    verify_path(test_img_path)
    test_img_basename = os.path.splitext(os.path.basename(test_img_path))[0]



    # take image path,  remove background, apply lapacian filter
    refPart_image_returned = rem_bg_lapacian(ref_img_path)
    cv2.imwrite(f'lapacian_{ref_imag_basename}.png', refPart_image_returned)  # save image with filter


    # take image path,  remove background, apply lapacian filter
    testPart_image_returned = rem_bg_lapacian(test_img_path)
    cv2.imwrite(f'lapacian_{test_img_basename}.png', testPart_image_returned)  # save image with filter

    # ORB alignment and detection 
    orb_alignment_detection(f'lapacian_{ref_imag_basename}.png',f'lapacian_{test_img_basename}.png')

    cv2.waitKey(0)
    cv2.destroyAllWindows()

