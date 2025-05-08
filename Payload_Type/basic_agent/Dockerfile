FROM itsafeaturemythic/mythic_python_base:latest
WORKDIR /Mythic/
COPY . .
RUN pip install requests pyinstaller
CMD ["python3", "main.py"]