# Stage 1: Build the application using the .NET 9 SDK
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build-env
WORKDIR /app

# Copy the csproj file and restore any packages
COPY *.csproj ./
RUN dotnet restore

# Copy the rest of the source code and build a Release publish output
COPY . ./
RUN dotnet publish -c Release -o out

# Stage 2: Create the lightweight runtime image
FROM mcr.microsoft.com/dotnet/aspnet:9.0
WORKDIR /app
COPY --from=build-env /app/out .

# Expose the default port for development/production
EXPOSE 5001
ENV ASPNETCORE_URLS=http://+:5001

ENTRYPOINT ["dotnet", "dotnet-service.dll"]