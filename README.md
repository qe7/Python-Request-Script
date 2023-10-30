# Python Request Script

This Python script provides a versatile tool for sending HTTP requests to a specified URL with custom options. It is designed to simplify interactions with web services and APIs, allowing you to control the number of requests, the rate at which they are sent, and the headers used in each request.

## Features

- **HTTP Request Sending**: Send HTTP requests to a specified URL, making it easy to access web resources and APIs.

- **Customization Options**: Control the number of requests, the rate of request sending (throttle time), and provide custom HTTP headers.

- **Concurrent Requests**: Utilize concurrent request handling through the use of threads, enabling efficient request processing.

## Usage

1. **Specify URL**: Enter the target URL to which you want to send HTTP requests.

2. **Set the Amount of Requests**: Define the number of requests you wish to send.

3. **Configure Workers**: Adjust the number of concurrent workers for parallel request execution. The recommended value is set to 8 workers.

4. **Set Throttle Time**: Specify the throttle time (in seconds) between each request. The recommended value is 1.5 seconds.

## Important

- Be mindful of the web service's usage policies and guidelines when making multiple requests. Excessive requests could lead to IP blocking or rate limiting.

## Requirements

- Python 3.6 or higher.

- `requests` library. You can install it using `pip install requests`.

## License

This script is released under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to contribute and improve this script. Your contributions are welcome!

