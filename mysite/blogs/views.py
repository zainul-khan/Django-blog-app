from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import CreateBlogSerializer, FetchBlogSerializer
from .models import Blog
from rest_framework.status import HTTP_200_OK

# Create your views here.
# class BlogView(viewsets.ModelViewSet):
#     def post(self, request):
#         try:
#             serializer_class= CreateBlogSerializer
#             return Response({"detail": "Post successfully"})


#         except Exception as e:
#             return Response({"detail": f"Something went wrong {str(e)}"})
        
#     def get(self, request):
#         try:
#             serializer_class= FetchBlogSerializer
#             fetch_all_blogs = Blog.objects.all()

#             return Response({
#                 'message': "Blogs fetched successfully",
#                 'data': fetch_all_blogs
#             },status = HTTP_200_OK)

#         except Exception as e:
#             return Response({"detail": f"Something went wrong {str(e)}"})


class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = FetchBlogSerializer  # Default serializer for listing and retrieving

    def create(self, request, *args, **kwargs):
        """Handle POST request to create a new blog"""
        try:
            serializer = CreateBlogSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Blog created successfully",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": f"Something went wrong: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        """Handle GET request to fetch all blogs"""
        try:
            blogs = Blog.objects.all()
            serializer = FetchBlogSerializer(blogs, many=True)
            return Response({
                'message': "Blogs fetched successfully",
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": f"Something went wrong: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        """Handle GET request to fetch a specific blog by ID"""
        try:
            blog = Blog.objects.get(pk=pk)
            serializer = FetchBlogSerializer(blog)
            return Response({
                'message': "Blog fetched successfully",
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response({"detail": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": f"Something went wrong: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """Handle PUT request to update a blog"""
        try:
            blog = Blog.objects.get(pk=pk)
            serializer = self.get_serializer(blog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': 'Blog updated successfully',
                    'data': serializer.data
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Blog.DoesNotExist:
            return Response({"detail": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": f"Something went wrong: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        """Handle DELETE request to delete a blog"""
        try:
            blog = Blog.objects.get(pk=pk)
            blog.delete()
            # serializer = FetchBlogSerializer(blog)
            return Response({
                'message': 'Blog deleted successfully'
            }, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response({"detail": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": f"Something went wrong: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)