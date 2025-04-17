% Define the folder where the original images are stored
source_folder = 'EE490'; % Replace with your folder path

% Define the folder where you want to save the convoluted images
output_folder = 'Convolved_test'; % Replace with your folder path
if ~exist(output_folder, 'dir')
    mkdir(output_folder);
end

% Define your convolution kernel (this is an example of an edge detection kernel)
kernel = [-1 0 -1; -1 0 -1; -1 0 -1]; % Replace with your kernel

% Get a list of all files in the folder
image_files = dir(fullfile(source_folder, '*.jpg')); % Adjust the extension if needed

for i = 1:length(4)
    image_path = 'EE490/nodisease/2.jpg'; %fullfile(source_folder, image_files(i).name);
    img = imread(image_path);
    
    % Check if the image is grayscale or color
    if size(img, 3) == 3 % If the image is RGB
        % Convert image to grayscale
        img_gray = rgb2gray(img);
    else
        img_gray = img;
    end
    
    % Apply convolution
    conv_img = conv2(double(img_gray), double(kernel), 'same');
    
    % Normalize the convoluted image to have values between 0 and 255
    conv_img = mat2gray(conv_img) * 255;
    
    % Plot the original and convoluted images
    figure;
    subplot(1,3,1), imshow(img), title('Original Image');
    subplot(1,3,2), imshow(img_gray), title('Grayscale Image');
    subplot(1,3,3), imshow(conv_img, []), title('Convolved Image');
    
    % Save the convoluted image to the output folder using saveas
    conv_fig = figure('visible', 'off'); 

    % Create axes in figure
    ax = axes('Parent', conv_fig, 'Position', [0 0 1 1], 'Visible', 'off');
    imshow(conv_img, []); % Display the convoluted image

    % Remove axis
    axis tight;
    axis off;
    axis image;

    output_filename = sprintf('%s_kernel.png', image_files(i).name(1:end-4));
    output_path = fullfile(output_folder, output_filename);
    saveas(conv_fig, output_path);

    close(conv_fig);
end
